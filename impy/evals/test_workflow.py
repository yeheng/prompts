import sys,json,copy,tempfile
import os
from pathlib import Path
os.chdir(Path(__file__).resolve().parent.parent)
sys.path.insert(0,str(Path('scripts').resolve()))
from workflow import validate,find
base=json.loads(Path('references/workflow.example.json').read_text());validate(base)
for change in [lambda d:d.update(status='completed'),lambda d:d['todos'][1].update(id=d['todos'][0]['id']),lambda d:d['todos'][0].update(status='blocked'),lambda d:d.update(updated_at='yesterday')]:
 d=copy.deepcopy(base);change(d)
 try:validate(d)
 except ValueError:pass
 else:raise AssertionError('accepted invalid checkpoint')
d=copy.deepcopy(base);d.update(status='completed',next_action=None)
for t in d['todos']:t.update(status='completed',note='Acceptance verified')
validate(d)
with tempfile.TemporaryDirectory() as tmp:
 root=Path(tmp); folder=root/'.impy/workflows';folder.mkdir(parents=True);d['workspace']=str(root);p=folder/'test.json';p.write_text(json.dumps(d));assert find(root)==[p.resolve()]
print('PASS: active/completed, four invalid states, checkpoint discovery')
import re
for p in [Path('SKILL.md'),*Path('references').glob('*.md')]:
 for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):assert (p.parent/link).exists(),(p,link)
print('PASS: all links')
