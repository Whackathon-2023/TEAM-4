import os
import openai

openai.api_type = "azure"
openai.api_base = "https://whackazureopenai4.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = "f06743f3d6024b488a38022f476ea726"

def query_ai(query, data):
    print(data)
    response = openai.ChatCompletion.create(
    engine="team4",
    messages = [{"role":"system","content":"You are an AI assistant that helps people find information."}, {"role": "user", "content": query + " answer this question using the following vessel JSON: " + data}],
    temperature=0.7,
    max_tokens=1000,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None)

    out = response['choices'][0]['message']['content'].replace("JSON", "database")
    out = out.replace("\n", "<br>")
    return out