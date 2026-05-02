import os
import time
from groq import Groq
from dotenv import load_dotenv
load_dotenv()


class GroqClient:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def generate_response(self, prompt):
        retries = 3

        for attempt in range(retries):
            try:
                response = self.client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )

                return response.choices[0].message.content

            except Exception as e:
                print(f"Error: {e}")

                if attempt < retries - 1:
                    time.sleep(2)

        return "Error generating response"