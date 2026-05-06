\# AI Demo Script



\## Demo Flow



\### 1. Health Check

Endpoint:

GET /health



Expected Output:

{

&#x20; "status": "healthy",

&#x20; "service": "ai-service",

&#x20; "model": "groq"

}



Purpose:

Shows AI service is running successfully.



\---



\### 2. Describe Endpoint

Endpoint:

POST /describe



Sample Input:

{

&#x20; "text": "Employee repeatedly violates security policy"

}



Expected Output:

{

&#x20; "input": "Employee repeatedly violates security policy",

&#x20; "output": "This is a placeholder AI response"

}



Purpose:

AI analyzes compliance-related text and generates description.



\---



\### 3. Recommend Endpoint

Endpoint:

POST /recommend



Expected:

3 structured recommendations in JSON format.



Purpose:

AI suggests corrective actions for compliance issues.



\---



\### 4. Generate Report Endpoint

Endpoint:

POST /generate-report



Expected:

Structured JSON report with summary and recommendations.



Purpose:

Automatically creates compliance reports.



\---



\## 60-Second Technical Explanation



This AI service is built using Flask in Python.



Groq API is used as the language model backend for generating AI responses.



Prompt templates are used to guide model responses into structured JSON outputs.



Docker is used to package the service for consistent deployment.



Security protections include:

\- input sanitization

\- prompt injection detection

\- rate limiting

\- environment variable protection



This makes the AI module portable, secure, and easy to integrate with Java backend services.

