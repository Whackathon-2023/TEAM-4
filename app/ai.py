#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai


class Chatbot():
    def __init__(self) -> None:
        self.token = 2000

        self.key = "f06743f3d6024b488a38022f476ea726"
    def call_chatbot(self, message):
        openai.api_type = "azure"
        openai.api_base = "https://whackazureopenai4.openai.azure.com/"
        openai.api_version = "2023-07-01-preview"
        openai.api_key = "f06743f3d6024b488a38022f476ea726"
        
        response = openai.ChatCompletion.create(
        engine="team4",
        messages = [{"role":"user","content":message}],
        temperature=0.7,
        max_tokens=self.token,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None)
     
        return response

