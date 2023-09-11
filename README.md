# Backend-Assesment-Yetti-Technolgies
Django Backend Developer Intern Assessment - Authentication and Testing


Creating a detailed README file is essential for project documentation and evaluation. Here's a sample README file with instructions on how to set up the project for evaluation and run the tests:

```markdown
# Django Authentication and Testing Example

This Django project demonstrates user authentication and testing using Django's built-in authentication system and testing framework. It includes user registration, login, logout, and secure access control to a "Hello World" page.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python (3.x recommended)
- Django
- Git (optional, for cloning the repository)

## Setup Instructions

1. Clone the repository (or download and extract the ZIP file):

   ```shell
   git clone https://github.com/yourusername/django-authentication-testing.git
   ```

2. Navigate to the project directory:

   ```shell
   cd django-authentication-testing
   ```

3. Create a virtual environment (optional but recommended):

   ```shell
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```shell
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```shell
     source venv/bin/activate
     ```

5. Install project dependencies:

   ```shell
   pip install -r requirements.txt
   ```

6. Migrate the database to create the necessary tables:

   ```shell
   python manage.py migrate
   ```

7. Create a superuser account (admin) to access the Django admin panel:

   ```shell
   python manage.py createsuperuser
   ```

8. Start the development server:

   ```shell
   python manage.py runserver
   ```

   The application should be accessible at `http://127.0.0.1:8000/`.

9. Access the admin panel:

   - Navigate to `http://127.0.0.1:8000/admin/`.
   - Log in with the superuser credentials created in step 7.

## Running Tests

To run the tests for the authentication system, execute the following command within the project directory:

```shell
python manage.py test yourappname
```

Replace `yourappname` with the name of the app where you added the tests (e.g., `myapp`). The tests will verify user registration, login, logout, access control, and basic security.

## Usage

- Register a new user at `http://127.0.0.1:8000/register/`.
- Log in with the registered user's credentials at `http://127.0.0.1:8000/login/`.
- Access the secure "Hello World" page at `http://127.0.0.1:8000/hello_world/`. Only authenticated users can access this page.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Your contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```