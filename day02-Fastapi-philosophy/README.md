## FastAPI Philosophy -  Day:02

This file is built on the core philosophy of FastAPI:

### 1. FAST API

FastAPI is a modern, high-performance web framework for building APIs with Python. It is built on two libraries:
- **Pydandtic:**  It checks that incoming data is correct and converts it into Python objects.
- **Starlette:** It is the lightweight ASGI web framework that handles requests, responses, routing, and asynchronous communication underneath FastAPI.

### 2. Philosophy

- **Fast to Run:** 
- **Fast to Code:**

### 2.1 Fast to Run

```text
┌────────────┐      ┌─────────────────────────────────────┐      ┌─────────────────────┐
│ Web Server │ ───► │ ASGI (Asynchronous Server Gateway)  │ ───► │      API Code       │
└────────────┘      └─────────────────────────────────────┘      └─────────────────────┘
       ⇓                            ⇓                                      ⇓
   Uvicorn                      Starlette                         Asynchronous Endpoint
```
**For Flask**
```text
┌────────────┐      ┌─────────────────────────────┐      ┌───────────────────┐
│ Web Server │ ───► │ WSGI (Gateway Interface)    │ ───► │ Flask Application │
└────────────┘      └─────────────────────────────┘      └───────────────────┘
       ⇓                         ⇓                                 ⇓
   Gunicorn                  Werkzeug                     Synchronous Endpoint
```

### 2.2 Fast to Code

- **Automatic API Documentation**: FastAPI automatically generates OpenAPI documentation and interactive Swagger UI without any additional configuration.
- **Automatic Input Validation**: Incoming data is automatically validated using Pydantic models. Developers do not need to write custom validation logic for common use cases.
- **Seamless Integration with Modern Ecosystem**: ML/DL libraries, SQL, Docker, Kubernetes etc.

---
