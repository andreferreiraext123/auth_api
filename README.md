# FastAPI Authentication Project

This project is a reusable FastAPI application for user authentication. It includes essential features such as user registration, login, and management of user data. The application is structured to promote modularity and maintainability.

## Project Structure

```
fastapi-auth-project
├── app
│   ├── api
│   │   ├── dependencies.py       # Reusable dependencies for the FastAPI application
│   │   ├── routes
│   │   │   ├── auth.py            # Authentication routes (login, registration)
│   │   │   └── users.py           # User-related routes (fetching, updating user info)
│   │   └── __init__.py
│   ├── core
│   │   ├── config.py              # Configuration settings (database URLs, secret keys)
│   │   ├── security.py            # Security functions (password hashing, JWT token generation)
│   │   └── __init__.py
│   ├── db
│   │   ├── base.py                # Base model for SQLAlchemy
│   │   ├── session.py             # Database session management
│   │   └── __init__.py
│   ├── models
│   │   ├── user.py                # User model representing the user table
│   │   └── __init__.py
│   ├── schemas
│   │   ├── auth.py                # Pydantic schemas for authentication
│   │   ├── user.py                # Pydantic schemas for user data
│   │   └── __init__.py
│   ├── main.py                    # Entry point of the application
│   └── __init__.py
├── tests
│   ├── test_auth.py               # Unit tests for authentication routes
│   ├── test_users.py              # Unit tests for user-related routes
│   └── __init__.py
├── .env                           # Environment variables for the application
├── .gitignore                     # Files and directories to be ignored by Git
├── requirements.txt               # List of dependencies required for the project
└── README.md                      # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd fastapi-auth-project
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install the dependencies:**
   ```
   pip install -r requirements.txt
   ```

5. **Set up environment variables:**
   Create a `.env` file in the root directory and add your configuration settings, such as database credentials and secret keys.

6. **Run the application:**
   ```
   uvicorn app.main:app --reload
   ```

## Usage Examples

- **Register a new user:**
  POST `/auth/register`
  
- **Login:**
  POST `/auth/login`

- **Fetch user details:**
  GET `/users/me`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.