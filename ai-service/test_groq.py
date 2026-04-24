from groq import Groq

client = Groq(api_key="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")

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": "Explain AI in simple words"}
    ]
)

print(response.choices[0].message.content)