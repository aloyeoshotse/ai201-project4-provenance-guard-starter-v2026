"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies. ← TODO

    Returns:
        A float. Decide yourself what scale it's on and which direction means
        "more human" — then write that down, because your combining rule
        depends on knowing it.

    A hint on what you're reaching for: the standard deviation of sentence
    lengths, probably divided by the mean so a long text and a short one are
    comparable. `statistics.stdev` is imported for you.

    Watch the edge case: a one-sentence submission has no spread at all, and
    `stdev` raises on fewer than two values. Decide what that should return
    before the attack set decides for you.
    """
    lengths = [len(words(s)) for s in sentences(text)]
    lengths = [n for n in lengths if n > 0]
    # One sentence has no spread to measure; return 0.0 and let
    # style_signal treat that case as "unknown" instead of "very even".
    if len(lengths) < 2:
        return 0.0
    mean = statistics.mean(lengths)
    # Coefficient of variation: spread relative to the mean, so a long text
    # and a short one are comparable. Higher means lumpier, more human.
    return round(statistics.stdev(lengths) / mean, 4)


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words. ← TODO

    Returns:
        A float between 0 and 1. Higher means more varied vocabulary.

    Worth knowing before you rely on it: this measure falls as text gets
    longer, because common words repeat. Two texts of different lengths aren't
    directly comparable on it, and if your test inputs vary a lot in length,
    that alone can look like a signal.
    """
    toks = words(text)
    if not toks:
        return 0.0
    # Only the first 100 words, so a long text isn't marked down for repeating
    # common words and a short one isn't flattered by having few to repeat.
    toks = toks[:100]
    return round(len(set(toks)) / len(toks), 4)


def punctuation_density(text: str) -> float:
    """
    How much punctuation, relative to length. ← TODO

    Returns:
        A float. Whether you count all punctuation or only some kinds — commas,
        semicolons, dashes — is a real choice. Semicolons and em dashes are
        more interesting than full stops, because they vary more between
        writers.
    """
    toks = words(text)
    if not toks:
        return 0.0
    # Everything except full stops: commas, semicolons, colons, dashes,
    # brackets, quotes, question and exclamation marks. Full stops just count
    # sentences, which sentence_length_spread already covers.
    marks = re.findall(r"[,;:()\"!?\u2014\u2013-]", text)
    # Per word, so length doesn't matter. Higher means more marks, more human.
    return round(len(marks) / len(toks), 4)


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.** ← TODO

    Combine your three measures into one number. Same direction as
    `detector.model_signal`, so that `scoring.combine_signals` can treat them
    the same way — if one of your signals runs backwards, everything above it
    is wrong in a way that's hard to see.

    Two things to decide and write down:

      1. Which direction each measure points. Low spread means more AI-ish, so
         it needs flipping. Work out which of your three need that.
      2. How to get each onto a comparable scale. A raw type-token ratio sits
         between 0 and 1; a raw punctuation count doesn't. Adding them
         unscaled means whichever has the bigger numbers wins by default.

    Test it on the four calibration inputs from Milestone 4 — clearly AI,
    clearly human, plain conventional human writing, lightly-edited AI — before
    you trust it. Plain and ordinary, not formal: formal prose reads as *human*
    to signal one, and it is plain writing that gets accused.
    """
    if len(words(text)) < 5:
        return 0.5   # too little text to see any shape: say "don't know"

    # Each raw measure is turned into an "AI-likeness" from 0 to 1 and clamped.
    # The anchors below are my judgment of where ordinary human and generated
    # text sit; they are decisions, and the README says so.

    # Spread: coefficient of variation. Human writing is lumpy, around 0.6 and
    # up; even, generated prose is around 0.3 or lower. One sentence is unknown.
    if len(sentences(text)) < 2:
        spread_ai = 0.5
    else:
        spread_ai = 1 - sentence_length_spread(text) / 0.7

    # Type-token ratio over the first 100 words. Varied vocabulary reads as
    # human, so a LOW ratio means more AI-like. Weak on short text.
    ttr_ai = (0.80 - type_token_ratio(text)) / 0.30

    # Punctuation beyond full stops per word. Plenty of varied marks is a sign
    # of a human hand, but having few is NOT a sign of AI: plain writers
    # (short sentences, second-language writers) use few marks too. So this
    # can only pull the score toward human; no marks at all is neutral (0.5).
    punct_ai = 0.5 * (1 - punctuation_density(text) / 0.15)

    def clamp(x):
        return min(max(x, 0.0), 1.0)

    score = (
        0.5 * clamp(spread_ai)
        + 0.2 * clamp(ttr_ai)
        + 0.3 * clamp(punct_ai)
    )
    return round(score, 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
    print("\nAll zeros? These are stubs — Milestone 4 is where you build them.")
