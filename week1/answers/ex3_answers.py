"""
Exercise 3 — Answers
====================
Fill this in after completing the three Rasa conversations.

CALM vs Old Rasa — what changed
---------------------------------
The old open-source Rasa approach used:
  - nlu.yml: intent training examples
  - rules.yml: explicit dialogue rules
  - FormValidationAction: Python class to parse slot values

Rasa Pro CALM uses:
  - flows.yml: natural language descriptions of what each flow does
  - from_llm slots: the LLM extracts values from conversation
  - ONE custom action: ActionValidateBooking for the business rules

The conversation is the same from the manager's perspective.
The machinery underneath is completely different.

CONVERSATION SCRIPTS
---------------------
Conversation 1 (happy path):
  You:    calling to confirm a booking
  Agent:  [asks guest count]
  You:    160 guests
  Agent:  [asks vegan count]
  You:    about 50 need vegan
  Agent:  [asks deposit]
  You:    £200 deposit
  Agent:  [confirms or escalates?]

Conversation 2 (deposit too high):
  Same as above but use a deposit above £300 (e.g. "£500 deposit").

Conversation 3 (out of scope):
  Start normally, then when asked for vegan count say something like
  "can you arrange parking for the speakers?" and observe what happens.
  Does CALM handle this differently than the old rules approach?
"""

# ── Conversation 1: Happy path ─────────────────────────────────────────────

CONVERSATION_1_TRACE = """
Your input ->  I am calling ot confirm the booking                               
How many guests are you confirming for tonight's event?
Your input ->  160                                                               
And how many of those guests will need vegan meals?
Your input ->  approximately 50                                                  
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  200 pounds                                                        
Thank you — booking confirmed. 160 guests, 50 requiring vegan meals, £200 deposit accepted. I'll send written confirmation to the organiser shortly.
Is there anything else I can help you with?
"""

CONVERSATION_1_OUTCOME = "confirmed"   # "confirmed" or "escalated"

# ── Conversation 2: Deposit too high ───────────────────────────────────────

CONVERSATION_2_TRACE = """
Your input ->  I am calling to confirm another booking                           
How many guests are you confirming for tonight's event?
Your input ->  160                                                               

Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers
Provider List: https://docs.litellm.ai/docs/providers




Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers
Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


And how many of those guests will need vegan meals?
Your input ->  50                                                                
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  500                                                               
Ok, I am updating guest_count, vegan_count to 160, 50 respectively.
I need to check one thing with the organiser before I can confirm. The issue is: a deposit of £500 exceeds the organiser's authorised limit of £300. Can I call you back within 15 minutes?
"""

CONVERSATION_2_OUTCOME = "escalated"   # "confirmed" or "escalated"
CONVERSATION_2_REASON  = "Requested deposit exceeds authorised limit"   # the reason the agent gave for escalating

# ── Conversation 3: Out of scope ───────────────────────────────────────────

CONVERSATION_3_TRACE = """
Your input ->  I need to confirm another booking                                 
How many guests are you confirming for tonight's event?
Your input ->  160 people and dogs                                               
I'm sorry, I'm not trained to help with that.
And how many of those guests will need vegan meals?
Your input ->  about 300                                                         
I'm sorry, I'm not trained to help with that.
I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly.
Would you like to continue with confirm booking?
Your input ->  yes                                                               
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  Do you have AV charges there?                                     
I'm sorry, I'm not trained to help with that.
I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly.
What deposit amount in GBP are you proposing to secure the booking?
"""

# Describe what CALM did after the out-of-scope message. Min 20 words.
CONVERSATION_3_WHAT_HAPPENED = """
After receiving the out-of-scope message the RASA agent just mentioned that they
couln't help with that and tried to repeat the previous question to keep the conversation on track.
"""

# Compare Rasa CALM's handling of the out-of-scope request to what
# LangGraph did in Exercise 2 Scenario 3. Min 40 words.
OUT_OF_SCOPE_COMPARISON = """
RASA handles out of scope requests with a fixed response that doesn't change 
based on the specific content of the user's message. 
It simply states that it can't help with that and tries to steer the conversation back 
to the expected flow. In contrast, LangGraph's handling of out-of-scope requests can be more 
dynamic, context-aware, and unpredictable as it can generate responses based on the specific 
content of the user's message and the overall conversation history. 
"""

# ── Task B: Cutoff guard ───────────────────────────────────────────────────

TASK_B_DONE = True   # True or False

# List every file you changed.
TASK_B_FILES_CHANGED = ["exercise3_rasa/actions/actions.py"]

# How did you test that it works? Min 20 words.
TASK_B_HOW_YOU_TESTED = """
I tested the cutoff guard by temporarily setting the condition to always True, 
running a conversation, and verifying it escalated.
"""

# ── CALM vs Old Rasa ───────────────────────────────────────────────────────

# In the old open-source Rasa (3.6.x), you needed:
#   ValidateBookingConfirmationForm with regex to parse "about 160" → 160.0
#   nlu.yml intent examples to classify "I'm calling to confirm"
#   rules.yml to define every dialogue path
#
# In Rasa Pro CALM, you need:
#   flow descriptions so the LLM knows when to trigger confirm_booking
#   from_llm slot mappings so the LLM extracts values from natural speech
#   ONE action class (ActionValidateBooking) for the business rules
#
# What does this simplification cost? What does it gain?
# Min 30 words.

CALM_VS_OLD_RASA = """
The simplification in Rasa Pro CALM reduces the amount of manual configuration and coding required to set up the agent.
The LLM can handle a wider variety of natural language inputs without needing explicit regex patterns or intent examples.
This allows for more flexibility and adaptability in conversations. 
However, it also means that the agent's behavior is less deterministic and may require more careful prompt engineering to ensure it behaves as expected. The gain is a more natural and flexible conversational experience, while the cost is potentially less control over the agent's responses and the need for more testing to ensure reliability.
Python still handles hard business rules and constraints, which is crucial for legally and financially binding decisions, 
while the LLM handles language understanding and slot extraction.
"""

# ── The setup cost ─────────────────────────────────────────────────────────

# CALM still required: config.yml, domain.yml, flows.yml, endpoints.yml,
# rasa train, two terminals, and a Rasa Pro licence.
# The old Rasa ALSO needed nlu.yml, rules.yml, and a FormValidationAction.
#
# CALM is simpler. But it's still significantly more setup than LangGraph.
# That setup bought you something specific.
# Min 40 words.

SETUP_COST_VALUE = """
The setup cost of Rasa Pro CALM is higher than LangGraph due to the need for multiple configuration files, 
training steps, and a Rasa Pro license. However, this setup allows for a more structured and controlled conversational 
agent that can handle complex dialogues and business rules. 
The specific value gained from this setup is the ability to create a more robust and reliable agent that can 
manage conversations in a way that is compliant with legal and financial requirements, 
while still leveraging the power of an LLM for natural language understanding.

Meanwhile, Lonagraph architecture allows to build agents with more natural, human-like conversation flow
It is also better suited for the scenarios with a wide variety of tools and complex multi-step reasoning, 
as it can dynamically decide which tools to call and when, without needing explicit flow definitions or slot mappings.

CALM agent can't improvise a response or use a tool that wasn'd defined in flows.yml, 
which is a limitation for handling unexpected user inputs or tasks that weren't anticipated during the design phase.
With Langraph, you can add tools dynamically.
"""
