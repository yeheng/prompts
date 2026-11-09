# Behavioral smoke evaluation

Three synthetic before/after Python fixtures, one trial per case per arm. Two fresh-context agents reviewed the same inputs; one loaded the saved skill, the other did not. Expected answers were withheld. Both agents handled all three cases in their own session, so cases within an arm were not independently isolated. Model settings and token usage were not captured; this is not a statistical benchmark.

## Results

| Behavior | With skill | Without skill |
|---|---|---|
| Guarded caller: avoid false positive | PASS | PASS |
| Zero-count regression: identify and reproduce | PASS | PASS |
| Pre-existing failure: do not attribute to change | PASS | PASS |

Grading is a manual comparison of reports against directly executed fixture behavior, not wording matching. Both arms found the single seeded defect and reported no introduced defects in the two negative cases. All six fixture files remained byte-identical. Ground-truth checks and raw reports are saved alongside this report.

## Observations and limits

The skill arm responded in Chinese, supplied a repair task, and preserved review-only boundaries. Both arms labeled the boundary defect P1, although the fixture provides no production severity context; severity calibration is not established by this test. The skill report correctly leaves negative-count requirements open but suggests count <= 0 as an option, which requires confirming intended behavior rather than treating it as the mandatory fix.

No demonstrated accuracy advantage over baseline: both arms pass these easy cases. No claims about repeatability, real-repository coverage, surgical implementation, blocked verification, or parallel integration are supported. Next run: add these harder scenarios, isolate each trial, repeat each arm, and capture model/configuration, timing, tokens, tool traces, and filesystem changes. Freeze the rubric before reruns and retain held-out cases.
