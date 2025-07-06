from strands import Agent
from strands_tools import use_aws

# Create an agent with default settings
agent = Agent(
    model="us.amazon.nova-micro-v1:0",
    tools=[use_aws],
)

# Ask the agent a question
agent("Tell me about agentic AI")
