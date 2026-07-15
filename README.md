# Web app with FastAPI

Web application build with FastAPI, HTML and CSS.

---

## Index

- [Overview](#overview)
- [Functionalities](#functionalities)
- [Used Technologies](#used-technologies)
- [Technical Decisions](#technical-decisions)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation and Configuration](#installation-and-configuration)
- [How to run locally](#how-to-run-locally)

---

## Overview

The web application API has one main page:

**Main (`/front`)** - App front main page

**Clients (`/clients`)** - Clients API page

**Client page (`/clients/<int:id>`)** - Client API page using the client's id

**Documentation (`/docs`)** - App documentation page

---

## Functionalities

- Front page using HTML
- Clients API with id, name, telefone, email connected to the sqlite
- A page for each client linked to the sqlite
- A client database with sqlite (CRUD)
- A HTTP request test file (CRUD Test)

---

## Used Technologies

| Technology | Function |
| --- | --- |
| Python 3.x | Main programming language |
| FastAPI | Framework web |
| Uvicorn | Asynchronous Web Server |
| SQLite  | Lightweight SQL Database |

---

## Technical Decisions

### Use FastAPI best practices for big project architecture

Use the FastAPI framework on the main.py and separated it in the app folder. Separate the client metadata in the models and routes folder, using POO architecture.

### Uvicorn

Bridge between the app and the network and used for tests.

### FastAPI Simplicity

The API made in FastAPI made the use and development very fast and simple.

### SQLite

Simple and lightweight SQL Database that integrates with python code.

### calls.http

calls.http file for testing HTTP requests: GET, POST, PUT, DELETE

---

## Project Structure

```
fastapi-app/
│
├── app/        # Global app configurations
│   ├── routes
│   │      └── client.py
│   ├── models
│   │      └── client.py
│   ├── database
|   |      ├── client_response.py
│   │      └── local.py
│   ├── dependences.py       # FastAPI dependences
│   └── main.py              # Main App
|
├── calls.http               # HTTP Requests Test File
├── local_database.db        # Main Database
├── README.md
└── requirements.txt         # Requirements
```

---

## Prerequisites

- Python 3.10 or superior
- Git
- pip

---

## Installation and Configuration

**1. Clone the repository**

```bash
git clone https://github.com/GMCavalheri/FastAPI-Web-app fastapi-app
cd fastapi-app
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

**3. install the requirements**

```bash
pip install -r requirements.txt
```

---

## How to run locally

```bash
uvicorn app.main:app --reload
```

Access the front page in the browser: [http://127.0.0.1:8000/front](http://127.0.0.1:8000/front)

Access the clients page in the browser: [http://127.0.0.1:8000/clients](http://127.0.0.1:8000/clients)

Access a client page using it's id, in the browser: [http://127.0.0.1:8000/clients/id](http://127.0.0.1:8000/clients/id)

Access the documentation in the browser: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
