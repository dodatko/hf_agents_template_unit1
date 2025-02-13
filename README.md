## Modified "First Agent Template" from [HuggingFace Agent Course: Unit 1](https://huggingface.co/learn/agents-course/unit1/tutorial)

Original template from Huggingface Spaces can found [here](https://huggingface.co/spaces/agents-course/First_agent_template).

The purpose and goal of the modifications:
* To run examples locally instead of on Hugging Face Spaces
* To demonstrate connecting to other models and providers via OpenRouter and test interactions with them
* … and since LiteLLM is used, not only with OpenRouter
* Replace the Gradio web interface with a simple CLI chat.  

## Setup and run
1. Clone this repo.
2. `cd` to cloned repo.
3. Copy `.env.example` to `.env` and add your API key for OpenRouter.


`python -m venv .venv`

`source .venv/bin/activate`

`pip install -r requirements.txt`

Run the agent: python app.py

Enjoy!
