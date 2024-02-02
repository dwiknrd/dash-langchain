from dash import Dash, dcc, html, callback, Input, Output
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI

import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
api_key = os.getenv("OPENAI_SECRET_KEY")
llm = ChatOpenAI(
    temperature=0.9,
    model_name="gpt-3.5-turbo-1106")


prompt_template = PromptTemplate.from_template("What is a good name for a brand that makes {product}?")

# prompt = prompt_template.format(product="burger")

# print(llm.predict(prompt))

app = Dash()

app.layout = html.Div([
    html.H1("Brand Name Generator"),
    html.Label("Your brand name: "),
    dcc.Input(id='subject', debounce=True, maxLength=15),
    html.Hr(),
    html.Div(id='brand_name')
])

@app.callback(
    Output('brand_name', 'children'),
    Input('subject', 'value'),
    prevent_initial_call=True
)
def update_layout(input_value):
    prompt = prompt_template.format(product=input_value)

    return llm.predict(prompt)

if __name__ == "__main__":
    app.run_server(debug=True)
