"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

# NOTE: criterion numbers follow criteria.md:
#   1 false positives   2 score spread   3 label coverage
#   4 appeal path       5 bad input
#
# The "human" texts below were drafted for this test, not taken from real
# people. Criterion 1 asks for writing you wrote yourself or collected from real
# people, so swap in your own pieces before trusting a result. The plain ones
# (short sentences, common words) are the ones that matter most.

PLAIN_HUMAN = [
    "I moved here in March. My new job starts at eight. I take the bus because I do not have a car. The bus is always full in the morning. I like my team. They are kind and they help me with my English. Sometimes I do not understand a word. Then I ask and they explain it.",
    "My brother has a small shop. He sells fruit and vegetables. He opens at six every day. I help him on Saturdays. We carry the boxes and put the apples in rows. The customers are friendly. Some of them bring their children. At the end of the day we are tired but we are happy.",
    "Yesterday it rained all day. I stayed at home and cleaned the kitchen. Then I made soup. I used potatoes, carrots and onions. It was not a special soup but it was warm. My sister called me in the evening. We talked for an hour about nothing important.",
    "The park near my house is small. There is a pond and a few benches. In the morning old men play chess there. In the afternoon children run around. I go there after work to sit down. I do not do anything. I just look at the trees and the water.",
]

NORMAL_HUMAN = [
    "Honestly the move was a disaster. The van showed up two hours late, the guy kept calling the sofa \"the beast\", and we lost a box labelled KITCHEN? that turned out to hold all my winter socks. Still, the new flat gets afternoon light and I found a bakery that does a decent pain au chocolat, so I'm calling it even.",
    "Gran's recipe never had amounts. It said things like 'enough flour' and 'bake till it looks right'. I ruined four loaves before Dad told me the secret, which was that she used the old tin and the oven ran hot. I still use the tin. It has a dent in one corner that shows up on every loaf.",
    "I failed my driving test twice, once for rolling through a stop sign and once, embarrassingly, for stalling in front of the examiner's own car. Third time I passed. My instructor cried a little. I think that was relief mostly, on his part.",
    "We argued about the thermostat all winter. He wanted 17, I wanted 21, and the compromise was me wearing two jumpers and him pretending not to notice the heater under my desk. Spring ended the war. Neither of us won.",
    "The match went to penalties and I couldn't watch, so I went and stood in the garden. I heard the whole street groan at once, then a single shout from number 12, then nothing. I had to ask the neighbour's kid who won.",
    "Dear Mr Hallam, I am writing about the fence between our gardens, which came down in the storm on the 14th. I would be glad to split the cost of a new one, though I would like to see two quotes first. I can be reached most evenings after six.",
]

AI_STYLE = [
    "Artificial intelligence has transformed the way organizations operate in the modern world. By leveraging advanced algorithms, businesses can streamline processes, enhance decision-making, and unlock new opportunities for growth. Furthermore, it is important to consider the ethical implications of these technologies. Ultimately, a balanced approach is essential to ensure that the benefits of AI are shared widely across society.",
    "Effective time management is a crucial skill for success in both personal and professional life. By prioritizing tasks, setting clear goals, and minimizing distractions, individuals can significantly improve their productivity. Moreover, maintaining a healthy work-life balance is essential for long-term well-being. In conclusion, mastering time management empowers people to achieve their objectives with confidence.",
    "Climate change represents one of the most pressing challenges of our time. Rising global temperatures contribute to extreme weather events, sea level rise, and loss of biodiversity. Addressing this issue requires collaborative action from governments, businesses, and individuals alike. By adopting sustainable practices and investing in renewable energy, we can build a more resilient future for generations to come.",
    "Remote work has fundamentally reshaped the modern workplace. It offers numerous benefits, including increased flexibility, reduced commuting time, and access to a broader talent pool. However, it also presents challenges such as communication barriers and feelings of isolation. Organizations that invest in strong digital infrastructure and foster a culture of trust are best positioned to thrive in this evolving landscape.",
    "Reading regularly provides a wide range of benefits for individuals of all ages. It expands vocabulary, improves concentration, and fosters empathy by exposing readers to diverse perspectives. Additionally, reading can reduce stress and promote better sleep. For these reasons, cultivating a daily reading habit is one of the most valuable investments a person can make in their personal growth.",
]

BORDERLINE = [
    "The meeting is on Thursday at ten. Please bring the signed forms and a copy of your ID. If you cannot come, let us know by Wednesday. We will send a reminder the day before. Parking is available behind the main building.",
    "Our team reviewed the results of the survey. Most respondents said they were satisfied with the service. A smaller group raised concerns about waiting times. We plan to look at staffing next month and report back.",
    "The new library opens next week. It has three floors and a small cafe. There are quiet rooms on the top floor for studying. Membership is free for residents. Opening hours are listed on the council website.",
]

SCENARIOS = [
    {
        "name": "own writing",
        "criterion": 1,
        # 10 human pieces, 4 of them deliberately plain.
        "texts": PLAIN_HUMAN + NORMAL_HUMAN,
    },
    {
        "name": "spread ai",
        "criterion": 2,
        "texts": AI_STYLE,
    },
    {
        "name": "spread human",
        "criterion": 2,
        "texts": NORMAL_HUMAN[:5],
    },
    {
        "name": "label coverage",
        "criterion": 3,
        # 3 intended human, 3 intended unsure, 3 intended AI, in that order.
        "texts": NORMAL_HUMAN[:3] + BORDERLINE + AI_STYLE[:3],
        "intended": ["human"] * 3 + ["unsure"] * 3 + ["ai"] * 3,
    },
    {
        # Needs a submission first, then an appeal. run_eval.py handles
        # scenarios marked "appeal": True itself.
        "name": "appeal path",
        "criterion": 4,
        "appeal": True,
        "texts": NORMAL_HUMAN + PLAIN_HUMAN,
    },
    {
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            {"creator_id": "eval_bad_missing"},
            {"text": "", "creator_id": "eval_bad_empty"},
            {"text": "   \n\t  ", "creator_id": "eval_bad_blank"},
            {"text": 12345, "creator_id": "eval_bad_number"},
            {"text": None, "creator_id": "eval_bad_null"},
            {"text": "word " * 20000, "creator_id": "eval_bad_huge"},
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
