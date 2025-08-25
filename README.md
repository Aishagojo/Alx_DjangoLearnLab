# Social Media API

A Django REST Framework-based API for a social media platform.

## Setup

1. Install dependencies: `pip install django djangorestframework Pillow`
2. Run migrations: `python manage.py migrate`
3. Start server: `python manage.py runserver`

## API Endpoints

- `POST /api/auth/register/` - Register a new user
- `POST /api/auth/login/` - Login and receive authentication token
- `POST /api/auth/logout/` - Logout and invalidate token
- `GET /api/auth/profile/` - Get user profile (requires authentication)
- `PUT /api/auth/profile/` - Update user profile (requires authentication)

## User Model

The custom user model extends Django's AbstractUser with:
- Bio (text field)
- Profile picture (URL field)
- Followers (many-to-many relationship to other users)

## Authentication

Uses token-based authentication. Include token in headers:
`Authorization: Token <your_token>`
