from strands import Agent
from strands_tools import use_aws
import re

# Create an agent with default settings
agent = Agent(
    model="us.amazon.nova-micro-v1:0",
    tools=[use_aws],
    callback_handler=None, # Suppresses debug output
    system_prompt="""
    あなたはAWSサービスの質問に答える有能なエージェントです。
    質問には簡潔に、50文字以内で回答してください。
    """
)

# Interactive loop to ask the agent questions
while True:
    user_input = input("\nYou: ")
    if user_input.strip().lower() in ("exit", "quit"):
        print("Exiting.")
        break
    if not user_input.strip():
        continue
    res = agent(user_input)
    if res is None:
        print("[debug] No response from the agent.")
    else:
        message = re.match(r"<(?:think|thinking)>(.*?)</(?:think|thinking)>(.*)", str(res), re.DOTALL)
        print(f"Agent: {message.group(2).strip() if message else res.strip()}")
