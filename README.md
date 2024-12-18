# 🌟 Python-Flask-Main Project 🌟

Welcome to the **Python Flask Microservices Project**, a robust implementation of a multi-service Flask-based application. This project is crafted to showcase microservices for **Authentication**, **Destination Management**, and **User Management**. 🚀

Each service operates **independently** with its own routes, models, and dedicated tests, ensuring modularity and scalability.

---

## 🗂️ Folder Structure

```
Python-Flask-Microservices-Project
|
├── Python-Flask-Main
│   |  
|   ├── authentication_service
│   |        ├── app.py
│   |        ├── models.py
│   |        ├── routes.py
│   |        └── tests
│   |              └── test_authentication_service.py
│   |
|   ├──  destination_service
│   |          ├── app.py
│   |          ├── controllers
│   |          │       └── destination_controller.py
│   |          ├── models
│   |          │       └── destination_model.py
│   |          │
|   |          ├── routes
|   |          |       └── destination_routes.py         
│   |          └── tests
│   |                  └── test_destination_service.py
│   |
|   └──  user_service
│   |       ├── app.py
│   |       ├── models
│   |       │       └── models.py
│   |       ├── routes
│   |       │       └── routes.py
│   |       └── tests
│   |               └── test_register.py
|   │
|   └── t.txt
├── README.md   
└──  venv
```

---

## 🌐 Project Highlights

- **Registration System**: Users can register their details, which are securely stored in `users.json`.
- **Authentication via JWT Tokens**: Upon successful login, a **JWT Token** is generated and saved in `tokens.json` for secure session management.
- **CRUD Operations**: Full destination management functionality.
- **Test-Driven Development (TDD)**: Each service is rigorously tested with `pytest`.

---

## 📜 Table of Contents

1. [Project Features](#-project-features)
2. [Services](#-services)
   - [Authentication Service](#authentication-service)
   - [Destination Service](#destination-service)
   - [User Service](#user-service)
3. [Setup Guide](#-setup-guide)
4. [How to Run](#️-how-to-run)
5. [Testing](#-testing)
6. [Folder Structure](#-folder-structure)
7. [Technologies Used](#-technologies-used)
8. [Future Enhancements](#-future-enhancements)
9. [Author](#-author)

---

## ✨ Project Features

- 🛡️ **Authentication**: User login generates JWT tokens, stored in `tokens.json`.
- 🗂️ **Data Management**: User details and tokens are persistently stored in JSON files (`users.json`, `tokens.json`).
- 🌍 **Destination Management**: In-memory CRUD operations for destinations.
- 🧪 **Comprehensive Testing**: Ensure all services work flawlessly using `pytest`.
- ⚡ **Microservices Architecture**: Separate and scalable services for different functionalities.

---

## 🛠️ Services

### 🌍 Destination Service

Manages destinations with descriptions, locations, and pricing.

#### **API Routes**

- **`GET /destinations`**: Fetches all available destinations.
- **`DELETE /destinations/<id>`**: Deletes a destination by ID (Admin access only).

#### **Features**

- Handles in-memory destination management.
- Provides admin-only deletion functionality.

#### **Test File**

- `test_destination_service.py`

---

### 🧑‍💻 User Service

Handles user registration and login processes.

#### **API Routes**

- **`POST /users/register`**: Registers a new user, storing details in `users.json`.
- **`POST /users/login`**: Authenticates users and generates JWT tokens which store in `tokens.json`.
- **`GET /users/profile`**: Retrieves user profiles using JWT tokens.

#### **Features**

- Secure password hashing with `bcrypt`.
- User information persistence in `users.json`.
- User token in `tokens.json`
- Role-based data handling for user profiles.

```
users.json
[
    {
        "name": "John Doe",
        "email": "john@example.com",
        "password": "$2b$12$GTG4OHpbXbv3B0G95pwaY.kSNps7Ef3NrFRABq/zxPKuX3k5Kdim.",
        "role": "User",
        "created_at": "2024-11-24T15:31:09.721546+00:00"
    },
    {
        "name": "kamran malik",
        "email": "kamran@example.com",
        "password": "$2b$12$drhamFBcjVPKujragFgC0Oqk8ajlb643HfoOa.hcUJF0V.1cSq6Xi",
        "role": "Admin",
        "created_at": "2024-11-24T15:32:40.600193+00:00"
    }
]
```
```
tokens.json
[
    {
        "email": "john@example.com",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImpvaG5AZXhhbXBsZS5jb20iLCJyb2xlIjoiVXNlciIsImV4cCI6MTczMjQ4MDI5NCwiaWF0IjoxNzMyNDYyMjk0fQ.xodlKM7KKhycwSgiO9d_2ZAP7uxWo1-klLV8RsjrzL8"
    },
    {
        "email": "kamran@example.com",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImthbXJhbkBleGFtcGxlLmNvbSIsInJvbGUiOiJBZG1pbiIsImV4cCI6MTczMjQ4MDM3OSwiaWF0IjoxNzMyNDYyMzc5fQ.Ppnp3LT1-8vkDQL5ZBbau2cotQObMRWoxkaP0_WiUFk"
    }
]
```
#### **Test File **

- `test_register.py`

---

### 🔑 Authentication Service

Collect **token** from `user_service` directory in `tokens.json` file and authenticate this token in this section so that it can handles user authentication and token validation.

#### **API Routes**

- **`POST /auth/validate`**: Validates a JWT token and retrieves associated user details.

#### **Features**

- Generates JWT tokens upon login.
- Validates and decodes JWT tokens.
- Manages tokens persistently in `tokens.json`.
![Alt text](aut.png)
![Alt text](aut1.png)


#### **Test File**

- `test_authentication_service.py`

---

# ⚙️ Setup Guide

### 1. **Clone the Repository**

```bash
git clone https://github.com/siam29/Python-Flask-Microservices-Project.git
```

### 2. **Activate the Virtual Environment**

```
python3 -m venv venv
source venv/bin/activate
```
### 3. **Main Directory**
```
cd Pyhon-Flask-main
```
### 4. **Install required dependencies**
```
pip install -r t.txt
```

## ▶️ How to Run each micro service

### 1. **Destination Service:**

```
cd destination_service
python app.py
```

### 2. **User Service:**

```
cd user_service
pip install bcrypt
python app.py
```

### 3. **Authentication Service**

```
cd authentication_service
python app.py
```

## 🧪 Testing

### Run Specific Service Tests

### 1. **Destination Service**

```
cd destination_service/tests
pip install pytest
pytest test_destination_service.py
```

### 2. **User Service**

```
cd user_service/tests
pytest test_register.py
```

### 3. **Authentication Service**

```
cd authentication_service/tests
pytest test_authentication_service.py
```
### 4. Code run on swagger
```
http://127.0.0.1:5000/apidocs/
```

---

### 🛠️ Technologies Used

- Python: Programming Language.
- Flask: Web Framework for creating REST APIs.
- Pytest: Testing Framework.
- JWT: JSON Web Token for authentication.
- JSON: Data storage for persistence.

### 🔮 Future Enhancements

- Transition from JSON to a relational database (e.g., SQLite, PostgreSQL).
- Implement role-based access control (RBAC) for improved security.
- Add Docker support for containerization.
- Expand unit testing for edge cases.

### 👤 Author

- **GitHub**: [https://github.com/siam29](https://github.com/siam29)
- **LinkedIn**: [https://www.linkedin.com/in/almahmud-siam-382a19206/](https://www.linkedin.com/in/almahmud-siam-382a19206/)

Feel free to connect and collaborate!
