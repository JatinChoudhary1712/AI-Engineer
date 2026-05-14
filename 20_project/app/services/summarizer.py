from app.services.openai_client import client


def summarize_text(text):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful summarizer."
            },

            {
                "role": "user",
                "content": f"Summarize this:\n{text}"
            }
        ]
    )

    return response.choices[0].message.content