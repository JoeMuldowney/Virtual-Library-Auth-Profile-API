# Virtual Library
This microservice creates an API using the Djanogo framework for built-in authentication.  Also, I utlized the Django framework using custom models implemnting user profiles, account features, and a book store. 

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies)

# Features

1. Authentication/Profile Model
   - Create, update, and delete users created by the user
   - Session cookies are used to track user logged in status and restrict features when the user is not logged in
   - Endpoints for user to update their profiles and accounts

2. Book Model
   - Offers one to many relationship between an authors table and a books table
   - Well defined endpoints to query books by category and get more details on a book by id
  
3. Account Feature Models
   - Utilize a one many relationship with the authentication table
   - Well defined endpoints to view saved books and get purchase history
      
# Technologies

1. Languages
   - Python
2. Frameworks
   - Django
3. Tools
   - Docker
   - Jenkins
   - Git
  

