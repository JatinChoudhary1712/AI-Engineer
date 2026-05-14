from app.services.openai_client import client


def sentiment_text(text):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",

        messages=[
            {
                "role": "system",
                "content": "You are a sentiment analyzer."
            },

            {
                "role": "user",
                "content": f"""
                Analyze the sentiment of this text.

                Return only one word:
                Positive, Negative, or Neutral.

                Text:
                {text}
                """
            }
        ]
    )

    return response.choices[0].message.content