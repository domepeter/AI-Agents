from openai import OpenAI, RateLimitError, APIError
from context import TWIN_SYSTEM_PROMPT
from tools import tools, handle_tool_calls, push
from styles import CSS, JS, EXAMPLES
from dotenv import load_dotenv
import gradio as gr

load_dotenv(override=True)

MODEL_NAME = "gpt-5.4-mini"
MAX_USER_MESSAGES = 10

openai = OpenAI()

system = [{"role": "system", "content": TWIN_SYSTEM_PROMPT}]


def chat(message, history):
    user_messages = sum(1 for m in history if m["role"] == "user")
    if user_messages >= MAX_USER_MESSAGES:
        return "Köszönöm a beszélgetést! Elértük az üzenetek maximális számát. Kérem vegye fel velünk a kapcsolatot a megadott elérhetőségek egyikén."

    push(f"New user message: {message[:900]}")
    messages = system + history + [{"role": "user", "content": message}]
    try:
        response = openai.chat.completions.create(model=MODEL_NAME, messages=messages, tools=tools)
        while response.choices[0].finish_reason == "tool_calls":
            message = response.choices[0].message
            tool_calls = message.tool_calls
            results = handle_tool_calls(tool_calls)
            messages.append(message)
            messages.extend(results)
            response = openai.chat.completions.create(model=MODEL_NAME, messages=messages, tools=tools)
        return response.choices[0].message.content
    except RateLimitError:
        push("OpenAI quota/rate limit hiba!")
        return "Sajnos most nem tudok válaszolni, elfogyott az egyenlegem."
    except APIError:
        return "Technikai hiba történt, kérlek, próbáld később."


if __name__ == "__main__":
    gr.ChatInterface(
        chat,
        examples=EXAMPLES,
        title="AI Assistant",
        description="Talk to my AI Assistant about my career! \n\n You might have to wait up to a minute for the first response while the app starts",
        chatbot=gr.Chatbot(show_label=False),
    ).launch(css=CSS, js=JS, theme=gr.themes.Base(), inbrowser=True)
