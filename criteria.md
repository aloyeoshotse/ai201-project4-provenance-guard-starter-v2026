# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. False positives: real writers are rarely called AI

Of 10 pieces I wrote myself or collected from real people, at most 1 is
labelled high-confidence AI. At least 3 of the 10 are deliberately plain
writing (short sentences, common words, the kind a second-language writer
produces). This must hold in each of the 3 trials, not on average.

**Why this target:** On a writing site, a wrong accusation costs a real person
a lot, and a missed AI text costs the site a little. I allow 1 in 10 because
perfect detection isn't possible, but I include plain writers on purpose,
since signal one is known to score them as machine-like. A test set of only
fluent prose would let me hit the number without testing the case that matters.

---

## 2. Score spread: clearly-AI and clearly-human text score apart

Across 5 clearly-AI texts and 5 clearly-human texts, the mean combined score of
the AI set is at least 0.30 higher than the mean of the human set. The AI set
averages above 0.60 and the human set averages below 0.40. Each of the 3 trials
meets all three conditions.

**Why this target:** My thresholds are 0.35 and 0.65. If the two groups don't
land on opposite sides of those lines, the labels mean nothing. A 0.30 gap is
large enough that noise from the model signal can't close it, but small enough
that I can reach it with two crude signals.

---

## 3. Label coverage: every label is reachable and none is a dead zone

Across a set of 9 inputs I chose to fall in each band (3 intended human,
3 intended unsure, 3 intended AI), all three labels appear at least once in
each of the 3 trials. At least 6 of the 9 inputs land in the label I intended.

**Why this target:** An unreachable label is a bug the writer never sees. A
weighted average of two signals can only land between them, so a flat style
signal quietly makes the human label unreachable. Requiring 6 of 9 to match my
intent checks that the bands mean something, and not just that each label
appears once.

---

## 4. The appeal path: an appeal always changes status and is always recorded

For 10 appeals on valid content_ids, 10 return HTTP 200, the item's status in
the log becomes `under_review`, and an appeal entry holding the writer's
reasoning exists in the log. An appeal on an unknown content_id returns 404
and records no appeal entry. This holds in each of the 3 trials, with no
exceptions.

**Why this target:** The appeal is the only thing between a wrong accusation
and nothing at all. It's a simple path with no model involved, so there's no
reason for it to ever fail. The target is 10 of 10 because any failure means a
wronged writer was told their appeal was received when it was not.

---

## 5. Bad input: malformed requests are refused, never crash

Five bad requests to `/submit` (no `text` field, empty string, whitespace
only, `text` as a number or null, and a 100,000-character string) each return
a 4xx status with a JSON `error` field. None returns a 500, none writes a
decision to the audit log, and `/health` still answers afterwards. This holds
in each of the 3 trials.

**Why this target:** A crash on malformed input is one of the most common real
failures, and the attack set will send exactly these. A refused request should
leave the service alive and the log unpolluted, so I check both.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
