# 🚀 FastAPI Patient API Project

This project is a simple **FastAPI-based REST API** that demonstrates how dynamic software works using CRUD operations on a patient dataset stored in a JSON file.

---

## 📚 Software Types

### Static Software

Static software delivers predefined content and functionality that remains largely unchanged unless manually updated by developers or administrators. The same information is typically presented to all users, with minimal processing or personalization.

**Examples:**
- Portfolio websites  
- Company landing pages  
- Documentation websites  
- Brochure websites  

---

### Dynamic Software

Dynamic software generates content and behavior based on user interactions, business logic, or data stored in databases. The information displayed can vary between users and may change in real time without modifying the application's source code.

**Examples:**
- E-commerce platforms  
- Social media applications  
- Banking systems  
- Learning Management Systems (LMS)  
- Customer Relationship Management (CRM) systems  

---

## 🔄 Dynamic Software Interaction Types (CRUD)

Dynamic software allows users to interact with data through four primary operations:

### ➕ Create (C)
Allows users to add new data to the system.

**Examples:**
- Registering a new account  
- Creating a blog post  
- Adding a product  

---

### 📖 Read (R)
Allows users to view or retrieve existing data.

**Examples:**
- Viewing a profile  
- Browsing products  
- Reading reports  

---

### ✏️ Update (U)
Allows users to modify existing data.

**Examples:**
- Editing profile information  
- Updating an order  
- Changing account settings  

---

### ❌ Delete (D)
Allows users to remove data from the system.

**Examples:**
- Deleting a post  
- Removing a product  
- Deactivating an account  

---

## 🌐 HTTP Methods Mapping

| CRUD Operation | HTTP Method |
|----------------|------------|
| Create         | POST       |
| Read           | GET        |
| Update         | PUT/PATCH  |
| Delete         | DELETE     |

---

# FastAPI Patient API Project

This project demonstrates a simple REST API using FastAPI with a JSON file as a mock database.

---

## 📁 Project Structure

```
fastapi-project/
├── main.py            # FastAPI application
├── patients.json      # Patient data (JSON file)
├── requirements.txt   # Project dependencies
```

## How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Tila173/fastapi-learning-journey.git
cd fastapi-learning-journey

2️⃣ Create virtual environment
python -m venv myenv
