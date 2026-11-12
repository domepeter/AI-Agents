from openai import OpenAI
from context import TWIN_SYSTEM_PROMPT
from tools import tools, handle_tool_calls
from styles import CSS, JS, EXAMPLES
from dotenv import load_dotenv
import gradio as gr

"""
load_dotenv(override=True)

openai = OpenAI(
    api_key=os.getenv("API_KEY"),      # "ollama" – dummy, de nem lehet üres
    base_url=os.getenv("BASE_URL"),    # http://localhost:11434/v1  ← ez irányít az Ollamára
)
model = os.getenv("MODEL")
"""

openai = OpenAI(api_key="ollama", base_url="http://localhost:11434/v1")
model = "qwen2.5:7b"

system = [{"role": "system", "content": TWIN_SYSTEM_PROMPT}]


def chat(message, history):
    messages = system + history + [{"role": "user", "content": message}]
    response = openai.chat.completions.create(model=model, messages=messages, tools=tools)
    while response.choices[0].finish_reason == "tool_calls":
        message = response.choices[0].message
        tool_calls = message.tool_calls
        results = handle_tool_calls(tool_calls)
        messages.append(message)
        messages.extend(results)
        response = openai.chat.completions.create(model=model, messages=messages, tools=tools)
    return response.choices[0].message.content


if __name__ == "__main__":
    gr.ChatInterface(
        chat,
        examples=EXAMPLES,
        title="Digital Twin",
        description="Talk to my AI twin about my career!",
        chatbot=gr.Chatbot(show_label=False),
    ).launch(css=CSS, js=JS, theme=gr.themes.Base(), inbrowser=True)
