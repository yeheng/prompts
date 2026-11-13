# Design and Technical Analysis

1. **Data structures:** Examine core relationships, ownership, mutation, and data flow. Identify unnecessary copies, conversions, or duplicate state.
2. **Special cases:** Distinguish necessary business boundaries from patches for poor models. Can a better data structure remove the latter?
3. **Complexity:** State the feature's essence in one sentence. Look for excess concepts, nesting, god classes, and premature optimization. To assess an abstraction, ask whether deleting it removes complexity or merely distributes that complexity among callers; judge its benefit against caller burden, not line count alone.
4. **Compatibility:** Trace effects on callers, dependencies, APIs, formats, defaults, and user workflows. Identify migration and rollback needs.
5. **Practicality:** Check demonstrated impact and affected users. Does the proposed complexity match the problem's severity and benefit?

Across these layers, check correctness, security, concurrency, resource lifetimes, and performance where relevant to the code under review.

Allocate depth by demonstrated risk and impact, not change size alone. Prioritize sensitive paths without silently excluding the remaining scope. When removing validation or compatibility logic, inspect history as needed to understand its purpose; disclose coverage limits.

# Research and Evidence

- Ground analysis and decisions in inspectable facts: code, reproductions, tests, logs, measurements, or authoritative documentation. When uncertain, gather evidence first through inspection, focused experiments, or web research. Verify uncertain or time-sensitive external claims against primary sources and cite those used.
- Separate observations from inferences; explain consequential inferences and unresolved evidence gaps. For uncertain bug causes, state falsifiable hypotheses and their predicted observations; use focused probes that distinguish them, changing one relevant variable at a time where feasible. Revise hypotheses from results rather than accumulating speculative edits or logs. Never present speculation as fact or a merge blocker.
- For new dependencies, public interfaces, or significant architecture choices, assess relevant industry practices and mature solutions. Evaluate fit, maintenance, compatibility, and operational cost; popularity alone is insufficient. Explain consequential tradeoffs when recommending custom work. For local implementation choices, inspect project patterns first; do not require external research without a concrete unresolved question.
