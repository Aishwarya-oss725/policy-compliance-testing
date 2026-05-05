# Policy Compliance Testing Project

## Overview
This project is a full-stack system for policy compliance testing with AI-based analysis, recommendation, and reporting features.

---

## Modules

### 1. Backend (Java + Spring Boot)
- REST APIs
- Authentication (JWT)
- Database integration
- Audit logging
- Security controls

### 2. Frontend (React)
- Dashboard UI
- Login system
- Search & filters
- Responsive design

### 3. AI Service (Flask)
- /describe endpoint
- /recommend endpoint
- /generate-report endpoint
- Mock AI responses for stability

---

## Tech Stack
- Java (Spring Boot)
- React (Vite)
- Python (Flask)
- REST APIs
- PowerShell testing

---

## AI Service APIs

### POST /describe
Returns description of input.

### POST /recommend
Returns structured recommendations.

### POST /generate-report
Returns structured analysis report.

---

## How to Run AI Service

```bash
cd ai-service
python app.py