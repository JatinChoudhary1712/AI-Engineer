from app.services.openai_client import client

def translate_text(text , language):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a text translator."
            },

            {
                "role": "user",
                "content": f"translate this:\n{text} in this language {language}"
            }
        ]
    )

    return response.choices[0].message.content