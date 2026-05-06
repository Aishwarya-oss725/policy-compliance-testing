\# AI Talking Points Card



\## AI Tech Stack



\- Python

\- Flask

\- Groq API

\- Docker

\- REST APIs



\---



\## What is Groq?



Groq is the AI provider used in this project.



Purpose:

\- Takes user input

\- Sends request to language model

\- Returns AI-generated output quickly



Used for:

\- Description generation

\- Recommendations

\- Report generation



\---



\## Prompt Flow



1\. User sends input text

2\. Flask endpoint receives request

3\. Prompt template is applied

4\. Request sent to Groq API

5\. AI response returned as JSON



\---



\## AI Endpoints



\### /health

Checks if AI service is running.



\### /describe

Generates AI description from input text.



\### /recommend

Returns recommended actions with priorities.



\### /generate-report

Creates structured compliance report.



\---



\## Security Talking Points



\- JWT authentication supported in integration

\- Input sanitization enabled

\- Prompt injection detection added

\- Rate limiting configured

\- API keys stored in environment variables



\---



\## Demo Explanation (Simple)



"Our AI service receives compliance-related input, sends it to Groq using structured prompts, and returns useful outputs such as descriptions, recommendations, and reports."

