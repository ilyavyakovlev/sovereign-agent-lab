"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ['search_venues', 'get_venue_details']

QUERY_1_VENUE_NAME    = "The Albanach"
QUERY_1_VENUE_ADDRESS = "2 Hunter Square, Edinburgh"
QUERY_2_FINAL_ANSWER  = "No available Edinburgh venues match these criteria."

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
The venue_server.py file was modified to update the status of venues.
The changes affected the availability of venues, 
which in turn impacted the results returned by the MCP client. 
No other files needed updating.

As a result, The Albanach was not returned as a fit, and the agent returned
an alternative venue: The Haymarket Vaults, which is available and meets the criteria.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 287   # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 231   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
MCP provides a structured and standardized way to define and manage tools,
enabling better modularity and separation of concerns. It allows for easier discovery and integration of tools,
as well as improved scalability and maintainability of the codebase.
With MCP, tools can be developed and updated independently, reducing the risk of unintended side effects on the main agent logic.
Additionally, MCP can facilitate better error handling and debugging by providing clear interfaces and logging for tool interactions.

MCP starts to shine specifically in the scenario when they are developed by 
an external provider and replace API calls to third-party services. In that case,
 the agent developer doesn't have to care about the implementation details
 of the tools and specifis of the API calls.
"""

# ── Week 5 architecture ────────────────────────────────────────────────────
# Describe your full sovereign agent at Week 5 scale.
# At least 5 bullet points. Each bullet must be a complete sentence
# naming a component and explaining why that component does that job.

WEEK_5_ARCHITECTURE = """
- FILL ME IN
- FILL ME IN
- FILL ME IN
- FILL ME IN
- FILL ME IN
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
FILL ME IN
"""
