import openai

api_key = "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"
def send_request(message):
openai.api_key = api_key
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",  messages=[{"role": "user", "content": message}])
        return chat_completion.choices[0].message['content']