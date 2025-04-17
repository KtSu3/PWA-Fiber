# PWA-Fiber

A modern web application for managing fiber-related data, built with a **Vue.js + Vite** frontend and a **Django-Ninja** backend. This project is split into two separate layers to ensure flexibility, maintainability, and performance.

---

## 🖥️ Project Structure

- **Backend**: Django-Ninja (Python)
- **Frontend**: Vue.js + Quasar CLI + Vite
- **Deployment Target**: Web (PWA) and Desktop (via PWA wrapping)

---

## 🔙 Backend - Django-Ninja

Built with [Django-Ninja](https://django-ninja.dev/), a fast and elegant web framework built on top of Django and Pydantic.

### ✅ Key Features:

- **Automatic API Documentation**: Swagger and Redoc support out of the box.
- **Asynchronous Endpoints**: Handles long-running tasks and heavy queries with better performance.
- **Fast Query Handling**: Optimized for speed and large datasets.
- **Strong Type Checking**: Thanks to Pydantic and Python type hints.
- **Clean API Design**: Easy to maintain and extend.
- **Built-in Security Features**: Auth, permissions, and input validation made simple.

---

## 🔐 Hidden Backend Files

Some backend files are **intentionally hidden or not included in the repository** for security and privacy reasons. These may include:

- Environment variable files (`.env`)
- Sensitive configuration files (e.g. database credentials, secret keys)
- Local-only scripts or data used during development

If you’re contributing or deploying the project, make sure to:

- Create a `.env` file with the required environment variables
- Set up your database credentials properly
- Follow any additional internal setup instructions if provided

> For more details or access to private configurations, please contact the project maintainer.


## 💻 Frontend - Vue.js + Vite + Quasar

A Progressive Web App (PWA) configured with the [Quasar Framework](https://quasar.dev/) and [Vite](https://vitejs.dev/) for fast development and lightning-speed builds.

### ✅ Key Features:

- **PWA Ready**: Works offline, installable on desktop and mobile, and optimized for performance.
- **Modular Architecture**: Reusable and encapsulated Vue components.
- **Responsive Design**: Adaptive layout for mobile, tablet, and desktop.
- **Fast Dev Build**: Thanks to Vite's hot module replacement.
- **Seamless API Integration**: Clean Axios services integrated with Django backend.
- **Quasar Components**: UI-rich and fully responsive with Material Design principles.

---

## 🚀 Getting Started

### Backend Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run server
python manage.py runserver
