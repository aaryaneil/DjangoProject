# Login System - Django Project

This project implements a basic login system using Django. The project handles user signup, login, and CRUD operations for managing user data. Below are the detailed steps for setting up the project, defining models, views, URLs, and performing CRUD operations.

---

## Task 1: Setting Up the Project

### 1.1 Create a Virtual Environment

### 1.2 Activate the Virtual Environment

### 1.3 Install Django

### 1.4 Create a New Django Project

### 1.5 Create a New Django Application

<img width="1440" alt="Screenshot 2024-10-14 at 2 23 54 PM" src="https://github.com/user-attachments/assets/6f5ac746-e836-4a0c-adb0-7984e6709480">


---

## Task 2: Create Views and URLs for Login System

### 2.1 Create Views

### 2.2 Define URL Patterns

<img width="1440" alt="Screenshot 2024-10-14 at 2 45 36 PM" src="https://github.com/user-attachments/assets/807b03fc-8eac-4947-a67d-4bc56e5ddbb4">
<img width="1440" alt="Screenshot 2024-10-14 at 2 45 29 PM" src="https://github.com/user-attachments/assets/1a4d53a9-997e-458d-9a6c-5acb69c8dce0">

---

## Task 3: Define Models for Login System

### 3.1 Create the `UserDetails` Model

### 3.2 Implement Signup and Login Views

### 3.3 Define URLs for Signup and Login

### 3.4 Create HTML Templates

---

## Task 4: Models & Admin

### 4.1 Set Up Superuser

### 4.2 Django Shell Commands for User Management


<img width="1440" alt="Screenshot 2024-10-14 at 3 04 58 PM" src="https://github.com/user-attachments/assets/ce1a2484-12a0-48c9-8f55-5b33e66709af">

<img width="1440" alt="Screenshot 2024-10-14 at 2 57 56 PM" src="https://github.com/user-attachments/assets/da7acc29-c3b2-47ed-bbb0-7022e6704b45">



---

## Task 5: CRUD Operations

### 5.1 CRUD Views

### 5.2 Define URL Patterns for CRUD Operations

### 5.3 Testing with Postman


### 1. **Get All Users**
To retrieve all user details, send a **GET** request:

```
GET http://127.0.0.1:8000/loginify/users/
```

Expected response:

<img width="1392" alt="Screenshot 2024-10-14 at 8 21 25 PM" src="https://github.com/user-attachments/assets/9dc0e2ff-8e25-4b5d-aa4d-b65f1cda7c35">



---

### 2. **Get User by Email**
To get details of a specific user by email, send a **GET** request:

```
GET http://127.0.0.1:8000/loginify/user/<email>/
```


Expected response:


<img width="1392" alt="Screenshot 2024-10-14 at 8 22 02 PM" src="https://github.com/user-attachments/assets/63f83e17-644c-49d4-9d4b-84e1fe457f8f">


---

### 3. **Update User Details**
To update a user’s details, send a **PUT** request to the update endpoint:

```
PUT http://127.0.0.1:8000/loginify/user/update/<email>/
```


Expected response:


<img width="1440" alt="Screenshot 2024-10-14 at 8 38 20 PM" src="https://github.com/user-attachments/assets/2e2c22e9-13be-435a-8a49-da74a267b88a">



---

### 4. **Delete User by Email**
To delete a user by their email, send a **DELETE** request:

```
DELETE http://127.0.0.1:8000/loginify/user/delete/<email>/
```

Expected response:


<img width="1392" alt="Screenshot 2024-10-14 at 8 24 49 PM" src="https://github.com/user-attachments/assets/023dd7de-c64b-43d2-b4d4-c2081f455d94">



---

### Summary

This project demonstrates how to build a simple login system in Django, handle user data using models, create views for user signup and login, and perform CRUD operations for managing users.
