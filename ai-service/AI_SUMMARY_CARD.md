# AI Summary Card

## Project
Policy Compliance Testing Tool - AI Service

---

## AI Endpoints

### 1. Health Check
**Endpoint:** GET /health

Purpose:
Checks whether AI service is active and healthy.

Sample Output:
```json
{
  "status": "healthy",
  "service": "ai-service",
  "model": "groq"
}
```

---

### 2. Describe Endpoint
**Endpoint:** POST /describe

Purpose:
Analyzes compliance-related text and generates AI description.

Sample Input:
```json
{
  "text": "Employee repeatedly violates company security policy"
}
```

---

### 3. Recommend Endpoint
**Endpoint:** POST /recommend

Purpose:
Generates recommended corrective actions.

Expected Output:
- action_type
- description
- priority

---

### 4. Generate Report Endpoint
**Endpoint:** POST /generate-report

Purpose:
Creates structured compliance report with summary and recommendations.

---

## Tech Stack

- Python
- Flask
- Groq API
- Docker
- REST API
- Prompt Engineering

---

## Security Features

- Input sanitization
- Prompt injection detection
- Rate limiting
- Environment variable protection

---

## GitHub Repository

https://github.com/Aishwarya-oss725/policy-compliance-testing