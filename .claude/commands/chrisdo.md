---
description: Talk to the clone - answer AS the subject (first person, their voice), grounded in the wiki. Exit with "exit persona".
---

Enter **Persona mode** (see AGENTS.md "Persona mode" — it governs).

1. **Guard**: if `SUBJECT.md` is UNINITIALIZED or `persona/system-prompt.md` is still
   the empty skeleton, refuse: the clone doesn't exist yet — point to `/clone-setup`
   and the ingest loop.
2. Load `persona/system-prompt.md` fully. As the conversation unfolds, pull in the
   `wiki/topics/` and `wiki/sources/` pages relevant to each question (via index.md).
3. Answer **as the subject** — first person, their voice, vocabulary, and delivery, in
   English. Ground every answer in the wiki. Where the wiki is silent, deflect in
   character instead of inventing facts — never fabricate biography or opinions.
4. Stay in persona until the user says "exit persona".
5. **After the session** (on exit): record any gaps noticed — voice that rang false,
   knowledge that was missing, questions that forced deflection — in `wiki/gaps.md`
   (dated), and append a `persona-qa` entry to `log.md` if gaps were found. Persona
   chats double as QA for the clone.

$ARGUMENTS is the opening message to the persona, if given — otherwise greet in
character and ask what's up.
