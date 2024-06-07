# Django Blog Project

This is a Django-based blog application where users can view the latest posts, all posts, and detailed views of individual posts.

## Features

- **Latest Posts**: Display the latest three posts on the homepage.
- **All Posts**: View all posts ordered by date.
- **Post Detail**: View details of a specific post using its slug.

## Technologies Used

- Django
- HTML/CSS for templates

## Getting Started

### Prerequisites

- Python 3.6+
- Django 3.2+

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations to set up the database:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser to access the Django admin:
    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:
    ```bash
    python manage.py runserver
    ```

### Project Structure

```plaintext
your-repository/
│
├── blog/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── blog/
│           ├── index.html
│           ├── all-posts.html
│           └── post-detail.html
├── your_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── README.md
└── requirements.txt

