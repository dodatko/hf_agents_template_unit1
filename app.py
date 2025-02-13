import os

from smolagents import CodeAgent,DuckDuckGoSearchTool, HfApiModel,load_tool,tool
import datetime
import requests
import pytz
import yaml
from tools.final_answer import FinalAnswerTool
from dotenv import load_dotenv
from Gradio_UI import GradioUI

# Below is an example of a tool that does nothing. Amaze us with your creativity !
@tool
def my_custom_tool(arg1:str, arg2:int)-> str: #it's import to specify the return type
    #Keep this format for the description / args / args description but feel free to modify the tool
    """A tool that does nothing yet 
    Args:
        arg1: the first argument
        arg2: the second argument
    """
    return "What magic will you build ?"


@tool
def calculator(number1:int, number2:int, operation:str)-> int:
    """A tool that performs calculations of two integer numbers
    Args:
        number1: the first number
        number2: the second number
        operation: calculation operation like '+', '-', other not supported
    """

    result = number1 + number2 if operation == "+" else number1 - number2

    return result

@tool
def get_current_time_in_timezone(timezone: str) -> str:
    """A tool that fetches the current local time in a specified timezone.
    Args:
        timezone: A string representing a valid timezone (e.g., 'America/New_York').
    """
    try:
        # Create timezone object
        tz = pytz.timezone(timezone)
        # Get current time in that timezone
        local_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        return f"The current local time in {timezone} is: {local_time}"
    except Exception as e:
        return f"Error fetching time for timezone '{timezone}': {str(e)}"


final_answer = FinalAnswerTool()
# model = HfApiModel(
#     max_tokens=2096,
#     temperature=0.5,
#     model_id='https://wxknx1kg971u7k1n.us-east-1.aws.endpoints.huggingface.cloud',# it is possible that this model may be overloaded
#     custom_role_conversions=None,
# )

from smolagents import LiteLLMModel
load_dotenv()
model = LiteLLMModel(
    # "openrouter/meta-llama/llama-3.2-3b-instruct",
    "openrouter/openai/gpt-4o-2024-11-20",
    temperature=0.5,
    api_key=os.environ["OPENROUTER_API_KEY"]
)

# Import tool from Hub
image_generation_tool = load_tool("agents-course/text-to-image", trust_remote_code=True)

with open("prompts.yaml", 'r') as stream:
    prompt_templates = yaml.safe_load(stream)
    
agent = CodeAgent(
    model=model,
    tools=[final_answer, get_current_time_in_timezone, calculator], ## add your tools here (don't remove final answer)
    max_steps=6,
    verbosity_level=1,
    grammar=None,
    planning_interval=None,
    name=None,
    description=None,
    prompt_templates=prompt_templates
)


# GradioUI(agent).launch()

# agent.run("sum 120 + 32, and after add 17")
# agent.run("What time is it now in Alicante?")

while True:
    user_input = input("User (or 'exit'): ")
    if user_input.lower().strip() == "exit":
        break
    response = agent.run(user_input)
    print("Agent answer: ", response)