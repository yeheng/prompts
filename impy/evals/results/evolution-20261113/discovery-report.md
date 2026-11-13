# Manual catalog selection evaluation
One blind manual trial; not actual host auto-routing. Decisions saved before expectations were read. Only skill frontmatter and case prompt/id were inspected before selection. No skill modification.

- impy-fix: selected=True; expected=True; match=True. Explicit Impy invocation for implementation.
- linus-review: selected=True; expected=True; match=True. Explicit Linus engineering review matches description.
- plain-fix: selected=False; expected=False; match=True. Generic fix request lacks named invocation or Linus style.
- nontechnical: selected=False; expected=False; match=True. 乐子 is casual nontechnical wording in poetry request; outside development scope.

Matches: 4/4. Single trial; no independent replication performed.
