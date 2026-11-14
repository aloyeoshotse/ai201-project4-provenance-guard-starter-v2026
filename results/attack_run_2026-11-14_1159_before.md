# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-14 11:59
- Auto-marked BROKE (5xx, crash, no response): **2**
- Left for you to judge: **54**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `b3b54725-4537-40b1-b2ce-e1660dfa11be` | human | 0.293 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `b0c1a96f-0ca7-4e5e-aeb4-3f9756d42d36` | unsure | 0.399 | HELD |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `3186e652-2dfe-45d7-9bcd-5bc33affc532` | unsure | 0.503 | HELD |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `1367d37d-7660-4818-aae1-d55a32c285d7` | unsure | 0.554 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `3ba1dd4d-76a5-4965-b85c-fbe8d9b3720a` | human | 0.234 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `29b39e18-3df7-4529-96c3-640f50cac415` | unsure | 0.404 | HELD |
| EV07 | evasion | signal two: padding with punctuation | 200 | `d43ced74-874b-4eaf-9556-d5df3ae4fb38` | unsure | 0.459 | HELD |
| EV08 | evasion | signal one: text below the token window | 200 | `a119826e-6e97-49c3-9822-2d8da5497e9a` | human | 0.326 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `0e73c989-1747-48d3-9e14-70b2d299bb89` | unsure | 0.527 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `d5c213a8-98e0-4ec5-80d7-2cdb591349b8` | ai | 0.815 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `b1803697-a2f2-4e56-9953-4d22162c8c35` | unsure | 0.519 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `9e28f95a-3476-4750-ae7d-d718dc53ad62` | ai | 0.653 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `05680465-7e9a-4cfa-8dcb-dccd6dc59b3a` | unsure | 0.640 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `44f290e9-3248-4d1d-a0cc-33a6e7ba5d2f` | unsure | 0.640 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `b3b57e89-023b-4415-a97a-c13bd0e4b850` | ai | 0.707 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `78d0fcad-6ea1-4fe7-b479-d84fd6ad5153` | unsure | 0.640 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `5a28dce3-75f2-427f-b9e7-3c715ba2026b` | unsure | 0.640 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `d4cbb31e-f748-4051-a812-4935e831de2f` | human | 0.330 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `e3ea50c1-60c5-4458-b0ed-5a9eb7d81c3b` | human | 0.348 | BROKE |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `80513e9d-3f61-498e-b498-99cfef4e66ab` | human | 0.179 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `0e1fc8de-6b4f-4eca-957d-febfe851b336` | unsure | 0.497 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `383840ba-e405-4689-9639-5e58e2bbe15e` | unsure | 0.415 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `75369f11-30ce-42a9-bf03-9d477083f81d` | unsure | 0.449 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `05244877-9d2a-490e-9855-0fb155e5d816` | unsure | 0.479 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `7b067b71-f393-40b8-bc2d-7ce570b68061` | human | 0.200 | HELD |
| MF04 | malformed | text is only punctuation | 200 | `f84443dd-f546-4894-b93b-691164b3717e` | human | 0.207 | HELD |
| MF05 | malformed | text is a very long single word | 200 | `6f9c2d70-be8d-437f-b907-8d2b4bbd5c4b` | ai | 0.799 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `846d58d2-955b-493b-b07b-bbbb2bfd49c8` | ai | 0.798 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `30b73a7f-0886-4fe7-8852-36416910da9d` | ai | 0.744 | BROKE |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | `58def46f-896e-4667-a388-a12fe13047a8` | human | 0.304 | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 200 | `13db87d0-575c-43d9-9bce-b27f791b4c1c` | human | 0.230 | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b466ba6c-07cc-4707-b613-d1ca4281e5f8` | human | 0.177 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c9686b3c-b4be-4707-984f-6a93c46f7f7d` | human | 0.177 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `dbba20a1-ab6d-4c42-a5c0-7da91d603ee3` | human | 0.177 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `47342824-93a0-4fe4-9d2f-78fcffec195e` | human | 0.177 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `af7af0ec-86a4-4265-beb5-1b9bfa9d5947` | human | 0.177 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `23338255-0e94-489b-a737-5ae09251aecb` | human | 0.177 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4394d621-2d1f-4107-9fcd-da39f779f7ed` | human | 0.177 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b0f9bb4f-e8b3-45b5-8d6b-64567fae80c8` | human | 0.177 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f8ae53f4-6d2a-4400-92c2-7186e27d6e8f` | human | 0.177 | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1317ba1b-6f03-4836-ad90-08fd20265387` | human | 0.177 | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 2 | 18 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "b3b54725-4537-40b1-b2ce-e1660dfa11be",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.2933,
  "model_score": 0.1635,
  "style_score": 0.4881,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "b0c1a96f-0ca7-4e5e-aeb4-3f9756d42d36",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.399,
  "model_score": 0.5943,
  "style_score": 0.106,
  "label": "We can't tell whether this was written by a person or with the help of AI. Our check isn't always right, especially on plain, simple writing, so please don't take this as a verdict. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "3186e652-2dfe-45d7-9bcd-5bc33affc532",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5028,
  "model_score": 0.6662,
  "style_score": 0.2578,
  "label": "We can't tell whether this was written by a person or with the help of AI. Our check isn't always right, especially on plain, simple writing, so please don't take this as a verdict. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "1367d37d-7660-4818-aae1-d55a32c285d7",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5539,
  "model_score": 0.6114,
  "style_score": 0.4676,
  "label": "We can't tell whether this was written by a person or with the help of AI. Our check isn't always right, especially on plain, simple writing, so please don't take this as a verdict. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "3ba1dd4d-76a5-4965-b85c-fbe8d9b3720a",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.2341,
  "model_score": 0.3212,
  "style_score": 0.1034,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "29b39e18-3df7-4529-96c3-640f50cac415",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4039,
  "model_score": 0.5727,
  "style_score": 0.1507,
  "label": "We can't tell whether this was written by a person or with the help of AI. Our check isn't always right, especially on plain, simple writing, so please don't take this as a verdict. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "d43ced74-874b-4eaf-9556-d5df3ae4fb38",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.4589,
  "model_score": 0.5862,
  "style_score": 0.2679,
  "label": "We can't tell whether this was written by a person or with the help of AI. Our check isn't always right, especially on plain, simple writing, so please don't take this as a verdict. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "a119826e-6e97-49c3-9822-2d8da5497e9a",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.3263,
  "model_score": 0.2452,
  "style_score": 0.448,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "0e73c989-1747-48d3-9e14-70b2d299bb89",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5273,
  "model_score": 0.7042,
  "style_score": 0.262,
  "label": "We can't tell whether this was written by a person or with the help of AI. Our check isn't always right, especially on plain, simple writing, so please don't take this as a verdict. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "d5c213a8-98e0-4ec5-80d7-2cdb591349b8",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.815,
  "model_score": 0.9792,
  "style_score": 0.5686,
  "label": "This may have been written with the help of AI. Our check can be wrong. If you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "b1803697-a2f2-4e56-9953-4d22162c8c35",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5187,
  "model_score": 0.6175,
  "style_score": 0.3705,
  "label": "We can't tell whether this was written by a person or with the help of AI. Our check isn't always right, especially on plain, simple writing, so please don't take this as a verdict. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "9e28f95a-3476-4750-ae7d-d718dc53ad62",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.6531,
  "model_score": 0.7387,
  "style_score": 0.5248,
  "label": "This may have been written with the help of AI. Our check can be wrong. If you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "05680465-7e9a-4cfa-8dcb-dccd6dc59b3a",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.64,
  "model_score": 0.8051,
  "style_score": 0.467,
  "label": "We can't tell whether this was written by a person or with the help of AI. Our check isn't always right, especially on plain, simple writing, so please don't take this as a verdict. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "44f290e9-3248-4d1d-a0cc-33a6e7ba5d2f",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.64,
  "model_score": 0.8329,
  "style_score": 0.3734,
  "label": "We can't tell whether this was written by a person or with the help of AI. Our check isn't always right, especially on plain, simple writing, so please don't take this as a verdict. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "b3b57e89-023b-4415-a97a-c13bd0e4b850",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7069,
  "model_score": 0.8005,
  "style_score": 0.5665,
  "label": "This may have been written with the help of AI. Our check can be wrong. If you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "78d0fcad-6ea1-4fe7-b479-d84fd6ad5153",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.64,
  "model_score": 0.8814,
  "style_score": 0.3073,
  "label": "We can't tell whether this was written by a person or with the help of AI. Our check isn't always right, especially on plain, simple writing, so please don't take this as a verdict. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "5a28dce3-75f2-427f-b9e7-3c715ba2026b",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.64,
  "model_score": 0.8816,
  "style_score": 0.3161,
  "label": "We can't tell whether this was written by a person or with the help of AI. Our check isn't always right, especially on plain, simple writing, so please don't take this as a verdict. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "d4cbb31e-f748-4051-a812-4935e831de2f",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.3297,
  "model_score": 0.3223,
  "style_score": 0.3407,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "e3ea50c1-60c5-4458-b0ed-5a9eb7d81c3b",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.3481,
  "model_score": 0.4625,
  "style_score": 0.1766,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "80513e9d-3f61-498e-b498-99cfef4e66ab",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.1786,
  "model_score": 0.2044,
  "style_score": 0.14,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "0e1fc8de-6b4f-4eca-957d-febfe851b336",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.4967,
  "model_score": 0.5943,
  "style_score": 0.3504,
  "label": "We can't tell whether this was written by a person or with the help of AI. Our check isn't always right, especially on plain, simple writing, so please don't take this as a verdict. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "383840ba-e405-4689-9639-5e58e2bbe15e",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4152,
  "model_score": 0.4998,
  "style_score": 0.2882,
  "label": "We can't tell whether this was written by a person or with the help of AI. Our check isn't always right, especially on plain, simple writing, so please don't take this as a verdict. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "75369f11-30ce-42a9-bf03-9d477083f81d",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.4494,
  "model_score": 0.6401,
  "style_score": 0.1633,
  "label": "We can't tell whether this was written by a person or with the help of AI. Our check isn't always right, especially on plain, simple writing, so please don't take this as a verdict. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "05244877-9d2a-490e-9855-0fb155e5d816",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.4793,
  "model_score": 0.5583,
  "style_score": 0.3608,
  "label": "We can't tell whether this was written by a person or with the help of AI. Our check isn't always right, especially on plain, simple writing, so please don't take this as a verdict. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "7b067b71-f393-40b8-bc2d-7ce570b68061",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.2,
  "model_score": 0.0,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "f84443dd-f546-4894-b93b-691164b3717e",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.2067,
  "model_score": 0.0112,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "6f9c2d70-be8d-437f-b907-8d2b4bbd5c4b",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.7986,
  "model_score": 0.9976,
  "style_score": 0.5,
  "label": "This may have been written with the help of AI. Our check can be wrong. If you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "846d58d2-955b-493b-b07b-bbbb2bfd49c8",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.7981,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "This may have been written with the help of AI. Our check can be wrong. If you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "30b73a7f-0886-4fe7-8852-36416910da9d",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.7438,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "This may have been written with the help of AI. Our check can be wrong. If you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "58def46f-896e-4667-a388-a12fe13047a8",
  "creator_id": null,
  "guess": "human",
  "confidence": 0.3037,
  "model_score": 0.2395,
  "style_score": 0.4,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "13db87d0-575c-43d9-9bce-b27f791b4c1c",
  "creator_id": {
    "id": "x"
  },
  "guess": "human",
  "confidence": 0.2295,
  "model_score": 0.0492,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;list&#39; object has no attribute &#39;get&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes",
  "verdict": "BROKE"
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "b466ba6c-07cc-4707-b613-d1ca4281e5f8",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1772,
  "model_score": 0.0287,
  "style_score": 0.4,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "c9686b3c-b4be-4707-984f-6a93c46f7f7d",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1772,
  "model_score": 0.0287,
  "style_score": 0.4,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "dbba20a1-ab6d-4c42-a5c0-7da91d603ee3",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1772,
  "model_score": 0.0287,
  "style_score": 0.4,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "47342824-93a0-4fe4-9d2f-78fcffec195e",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1772,
  "model_score": 0.0287,
  "style_score": 0.4,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "af7af0ec-86a4-4265-beb5-1b9bfa9d5947",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1772,
  "model_score": 0.0287,
  "style_score": 0.4,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "23338255-0e94-489b-a737-5ae09251aecb",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1772,
  "model_score": 0.0287,
  "style_score": 0.4,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "4394d621-2d1f-4107-9fcd-da39f779f7ed",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1772,
  "model_score": 0.0287,
  "style_score": 0.4,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "b0f9bb4f-e8b3-45b5-8d6b-64567fae80c8",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1772,
  "model_score": 0.0287,
  "style_score": 0.4,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "f8ae53f4-6d2a-4400-92c2-7186e27d6e8f",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1772,
  "model_score": 0.0287,
  "style_score": 0.4,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "1317ba1b-6f03-4836-ad90-08fd20265387",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1772,
  "model_score": 0.0287,
  "style_score": 0.4,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
