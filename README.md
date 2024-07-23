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

## Testing
To run tests and check coverage Pytest is installed in the application for testing the application and is recommended by python. To run the test cases run this command in the root of the folder

- Install Testing Dependencies:

```
pip install pytest pytest-django
```

- Run Tests:
```
cd contactsApiMySql
cd contacts_api
pytest
```

- Check Test Coverage:
```
pytest --cov
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

<img width="1000" alt="image" src="https://github.com/user-attachments/assets/b5dc6409-5f99-46b8-8248-a1d587fd7a95">

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

<img width="1000" alt="image" src="https://github.com/user-attachments/assets/d854bbec-18d6-492d-8942-a8aff0f4a7bc">


### Crud APIs

These api needs authenticated users for performing the crud operations. After login use the token received from login in header of other APIs.

```
Authorization : Bearer <Token>
```

- Contacts List

GET /contacts/

Desc: Retrieves a list of all contacts.

<img width="1000" alt="image" src="https://github.com/user-attachments/assets/59c3c3eb-bcce-4852-a641-011306aa5d79">

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

<img width="1000" alt="image" src="https://github.com/user-attachments/assets/ea48582c-187d-4bb7-969e-15c998168166">


- Retrieve Contact

GET /contacts/{id}/

Desc: Retrieves a specific contact by ID.

<img width="1000" alt="image" src="https://github.com/user-attachments/assets/55959a73-8381-4877-bdfb-54096afd42ae">

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

<img width="837" alt="image" src="https://github.com/user-attachments/assets/a7048e7c-fd1f-4f5a-b2a4-f400bd16dccf">

- Delete Contact

DELETE /contacts/{id}/

Desc: Deletes a specific contact by ID.

<img width="831" alt="image" src="https://github.com/user-attachments/assets/962547d7-601a-440d-b20f-abfbefb0dcdc">


Request and Response Formats
Request Format: JSON
Response Format: JSON

### Project Structure
`contacts/`: Contains the Django app for contacts management.

models.py: Defines the Item and Supplier models.
views.py: Contains API views for items and suppliers.
serializers.py: Serializers for the models.
permissions.py: permissions for users and roles
utils.py: Utility functions for JWT creation and decoding

`contacts_api/`: Project settings and configuration.

settings.py: Configuration settings.
urls.py: Project-wide URL routing.


