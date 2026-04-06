# AI-Assisted Study Companion

An AI-powered study platform that helps students learn smarter by generating summaries, quizzes, progress analytics, and interactive tutoring from uploaded study materials.

---

## Features

* Session-based Authentication (Email Verification & Password Reset)
* Subject Management
* Study Material Upload (PDF/DOC)
* AI Summary Generation
* AI Quiz Generator
* Progress Tracking Dashboard
* AI Study Chatbot
* Study Activity Analytics

---

## Tech Stack

**Frontend**

* React.js
* Axios (with session cookies)

**Backend**

* Django
* Django REST Framework
* Session Authentication

**AI**

* LLM-based summarization, quiz generation, and tutoring

---

## Base API

```
http://127.0.0.1:8000/api/
```

Frontend requests use:

```js
axios({ withCredentials: true })
```

---

## API Endpoints

### Authentication

```
POST /auth/register/
GET  /auth/verify-email/<uid>/<token>/
POST /auth/login/
POST /auth/logout/
GET  /auth/me/
POST /auth/password-reset/
POST /auth/password-reset-confirm/
```

### Subjects

```
GET /subjects/
```

### Study Materials

```
POST   /materials/upload/
GET    /materials/
GET    /materials/<id>/
DELETE /materials/<id>/
```

### AI Features

```
POST /ai/summary/
GET  /ai/summary/<material_id>/

POST /ai/quiz/
GET  /quizzes/<id>/
POST /quizzes/submit/
```

### Progress & Dashboard

```
GET /progress/
GET /progress/<subject_id>/
GET /dashboard/
```

### Chatbot

```
POST   /chat/
GET    /chat/history/
DELETE /chat/history/
```

### Activity

```
GET /activity/
```

---

## Installation

### Backend

```
cd backend
python -m venv venv
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend

```
cd frontend
npm install
npm start
```

---

## Environment Variables

Create `.env` file:

```
SECRET_KEY=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
OPENAI_API_KEY=
```

---

## Workflow

**Backend**

* Handles authentication
* Manages database
* Communicates with AI
* Protects API endpoints

**Frontend**

* Sends requests
* Displays results
* Handles UI & navigation

---

## Purpose

This project demonstrates a complete **full-stack AI application** including authentication, REST APIs, file processing, and AI integration.

---
