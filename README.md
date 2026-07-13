# Books REST API with Flask

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

**Documentation (`/docs`)** - App documentation page

---

## Functionalities

- Front page using HTML

---

## Used Technologies

| Technology | Function |
| --- | --- |
| Python 3.x | Main programming language |
| FastAPI | Framework web |

---

## Technical Decisions

Use the FastAPI framework on the main.py and separated in the app folder

### FastAPI Simplicity

The API made in FastAPI made the use and development very fast and simple.

---

## Project Structure

```
fastapi-app/
│
├── app/        # Global app configurations
│   └── main.py              # Main App
|
├── README.md
└── requirements.txt
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

Access the documentation in the browser: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
