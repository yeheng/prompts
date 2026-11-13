"""Validate checkpoints or find them: python3 workflow.py validate FILE | find WORKSPACE."""
import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path


def validate(data):
    schema = json.loads((Path(__file__).resolve().parent.parent / 'references/workflow.schema.json').read_text())

    def check(value, spec, location):
        types = {'object': dict, 'array': list, 'string': str, 'null': type(None)}
        expected = spec.get('type', [])
        expected = [expected] if isinstance(expected, str) else expected
        if expected and not any(isinstance(value, types[t]) for t in expected):
            raise ValueError(f'{location}: invalid type')
        if 'enum' in spec and value not in spec['enum']:
            raise ValueError(f'{location}: invalid status')
        if isinstance(value, dict):
            if set(spec.get('required', [])) - value.keys():
                raise ValueError(f'{location}: missing fields')
            if spec.get('additionalProperties') is False and value.keys() - spec['properties'].keys():
                raise ValueError(f'{location}: unknown fields')
            for key, item in value.items():
                check(item, spec['properties'][key], f'{location}.{key}')
        elif isinstance(value, list):
            if len(value) < spec.get('minItems', 0):
                raise ValueError(f'{location}: empty list')
            for item in value:
                check(item, spec['items'], location + '[]')
        elif isinstance(value, str):
            if len(value) < spec.get('minLength', 0):
                raise ValueError(f'{location}: empty string')
            if spec.get('format') == 'date-time':
                if 'T' not in value or datetime.fromisoformat(value.replace('Z', '+00:00')).tzinfo is None:
                    raise ValueError(f'{location}: timestamp needs timezone')

    check(data, schema, 'workflow')
    todos = data['todos']
    if len({t['id'] for t in todos}) != len(todos):
        raise ValueError('duplicate todo IDs')
    for todo in todos:
        if todo['status'] in ('completed', 'skipped', 'blocked') and not (todo['note'] or '').strip():
            raise ValueError('completed/skipped/blocked todo needs a result or reason')
    terminal = data['status'] in ('completed', 'cancelled')
    if terminal and data['next_action'] is not None:
        raise ValueError('terminal workflow must have null next_action')
    if not terminal and not (data['next_action'] or '').strip():
        raise ValueError('unfinished workflow needs next_action')
    if data['status'] == 'completed' and any(t['status'] not in ('completed', 'skipped') for t in todos):
        raise ValueError('completed workflow has unresolved todos')


def find(workspace):
    root = Path(workspace).resolve()
    key = hashlib.sha256(str(root).encode()).hexdigest()[:16]
    locations = [root / '.impy/workflows', Path.home() / '.impy/workflows' / key]
    matches = []
    for location in locations:
        for path in sorted(location.glob('*.json')):
            try:
                data = json.loads(path.read_text())
                validate(data)
                if Path(data['workspace']).resolve() == root:
                    matches.append(path.resolve())
            except (ValueError, OSError) as error:
                print(f'Invalid checkpoint {path}: {error}')
    return matches


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['validate', 'find'])
    parser.add_argument('path')
    args = parser.parse_args()
    try:
        if args.action == 'validate':
            validate(json.loads(Path(args.path).read_text()))
            print('Valid checkpoint')
        else:
            for match in find(args.path):
                print(match)
    except (ValueError, OSError) as error:
        parser.exit(1, f'{error}\n')
