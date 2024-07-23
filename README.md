# Contact Management System

A simple contact management system built with Django. This project allows you to add, view, update, and delete contacts. It includes APIs for interacting with the contact data and uses environment variables to manage keys, database settings securely.

## Features

- Add new contacts
- View a list of all contacts
- Edit existing contacts
- Delete contacts
- Secure database configuration using environment variables
- SignIn and SignUp functionality (Auth using JWT)

## Requirements

- Python 3.6 or higher
- Django 3.0 or higher
- MySQL (or any other supported database)

## Installation

1. **Clone the repository**

 ```bash
 git clone https://github.com/abhishek-bhatt-consultadd/crud-app-django.git
 cd contacts_api
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate 
```
3. **Install the dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a .env file in the root directory of the project with the following content:

```
DB_ENGINE='django.db.backends.mysql'
DB_NAME='db_name'
DB_USER='user_name'
DB_PASSWORD='your_password'
DB_HOST='127.0.0.1' // default for sql
DB_PORT='3306'
```

5. **Apply database migrations**

```
python manage.py makemigations
python manage.py migrate
```

6. **Run the development server**

```
python manage.py runserver
You can now access the application at http://127.0.0.1:8000/.
```
7. **Run test**

Pytest is installed in the application for testing the application and is recommended by python. To run the test cases run this command in the root of the folder

```
cd contactsApiMySql
cd contacts_api
pytest
```

## API Documentation
The Contact Management System provides a RESTful API for managing contacts. The API is built using Django REST Framework.

BASE URL: 
http://127.0.0.1:8000/

### Authentication

- Sign Up

POST /signup/

Desc: Registers a new user. The request body should include:

```
{
    "username": "newuser",
    "password": "password123",
}
```

- Log In

POST /login/

Authenticates a user. The request body should include:

```
{
    "username": "newuser",
    "password": "password123"
}
```

Response:
On success:
```
{
    "token": "your_jwt_token_here",
}
```
On error:

```
{
    "error": "Invalid username or password"
}
```

### Crud APIs

These api needs authenticated users for performing the crud operations. After login use the token received from login in header of other APIs.

```
Authorization : Bearer <Token>
```

- Contacts List

GET /contacts/

Desc: Retrieves a list of all contacts.

- Create Contact

POST /contacts/

Desc: Creates a new contact. The request body should include:

```
{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone": "+1234567890",
    "add" : "IN"
}
```

- Retrieve Contact

GET /contacts/{id}/

Desc: Retrieves a specific contact by ID.

- Update Contact

PUT /contacts/{id}/

Desc: Updates an existing contact. The request body should include:

```
{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone": "+0987654321",
    "add" : "WA"
}
```

- Delete Contact

DELETE /contacts/{id}/

Desc: Deletes a specific contact by ID.

Request and Response Formats
Request Format: JSON
Response Format: JSON

