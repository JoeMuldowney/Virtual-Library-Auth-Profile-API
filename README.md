# Virtual Library
This microservice provides an API using the Django framework, featuring built-in authentication. It includes custom models for user profiles, account management, and a book store.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies)

# Features

1. **Authentication/Profile Model**
   - Create, update, and delete user accounts
   - Session cookies are used to track login status and restrict access to features when not logged in
   - Endpoints for users to update their profiles and account details

2. **Book Model**
   - Implements a one-to-many relationship between authors and books
   - Well-defined endpoints to query books by category and retrieve book details by ID
  
3. **Account Feature Models**
   - Utilizes a one-to-many relationship with the authentication table
   - Well-defined endpoints to view saved books and access purchase histor
      
# **Technologies**

1. **Languages**
   - Python
2. **Frameworks**
   - Django
3. **Tools**
   - Docker
   - Jenkins
   - Git
  

