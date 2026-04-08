"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True   # True or False
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
We see that all three ways to format the context led to correct answers due to the small size of the returned values
by the mock tool and strong underlying LLM performance. 
Generally, we expected the XML and sandwich formatting to perform better than the plain formatting, but in this case all three performed equally well.
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_B_XML_ANSWER      = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
The Holyrood Arms must have been the hardest distractor because its status="full" could misled the model into thinking it was unavailable.
It is also placed very close to one of the needles.
All of this is hypothetical, because the experiment under the following conditions showed that all three approaches performed well.
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True   # True or False

PART_C_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
Despite downgrading the the model to a smaller one, it was able to provide the correct unswer under all 3 experiments.
Also, we see that it returned the Haymarket Vaults in all three cases, which is surprising, as it is not the first correct
value in the list. I think this experiment teaches us the fact that simpler models prioritise the recent context more than the older context, which is a good thing in this case, as the most recent context is more relevant to the question.
more sophisticated ones. Fore larger models, structuring the context helps it to focus less on the recent context.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
Context formatting matter in the following cases:
1. Operating smaller models, which are more likely to be misled by distractors or less able to focus on the old context.
2. When the needles are hidden among a large number of distractors nearby.
3. When the context is large and contain a lot of misleading /  distracting information.
"""
