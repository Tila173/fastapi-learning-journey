# Day 01 — APIs, Architecture & FastAPI Intro

## What is an API?
APIs (Application Programming Interfaces) are contracts that allow two systems
to communicate. Instead of sharing code or databases directly, systems talk
through defined endpoints.

**Real-world analogy:** A waiter in a restaurant — you (client) don't go to the
kitchen directly. The waiter (API) takes your request and brings back the response.

---

## Why Do We Need APIs?
- Separation of concerns between frontend and backend
- Different teams/languages can work independently
- Reusability — one backend can serve web, mobile, third-party clients

---

## Monolithic Architecture
Everything (UI, business logic, database) lives in one codebase and is deployed together.

**Problems:**
- One bug can crash the whole system
- Hard to scale individual parts
- Slow deployments — a small change requires redeploying everything
- Teams step on each other's code

---

## Tightly Coupled vs Decoupled
| | Tightly Coupled | Decoupled |
|---|---|---|
| Dependency | Components depend directly on each other | Communicate via interfaces/APIs |
| Change impact | Change one → breaks others | Change one → others unaffected |
| Example | Monolith | Microservices |

---

## FastAPI Architecture
FastAPI is built on:
- **Starlette** — for the web/async layer
- **Pydantic** — for data validation
- **Uvicorn** — ASGI server that runs it

Request flow:
`Client → Uvicorn → Starlette Router → Your Route Function → Pydantic Validation → Response`

---

## Key Takeaways
- APIs decouple systems so they can evolve independently
- Monoliths work small but become painful at scale
- FastAPI gives you speed + automatic docs out of the box
