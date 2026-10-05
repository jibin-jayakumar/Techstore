# TechStore — Django E-Commerce Website

A dynamic e-commerce website built with Django, inspired by the Apple Store experience.

## Live Demo

- **Website:** https://techstore-sle0.onrender.com/
- **Admin Panel:** https://techstore-sle0.onrender.com/admin/

## Credentials

### Admin
- Username: `admin`
- Password: `Admin@12345`

### Test User
- Username: `testuser`
- Password: `TestPass123!`

## Features

- **Dynamic Homepage** — hero banners, featured products, categories, promotions, footer — all database-driven
- **Product Catalog** — browse all products, filter by category, individual detail pages
- **Admin Panel** — full CRUD for Products, Categories, Banners, Promotions, and Users via Django Admin
- **User Authentication** — registration, login, logout, protected profile page using Django's built-in session auth
- **Responsive Design** — mobile-friendly layout using CSS Grid and Flexbox

## Tech Stack

- **Backend:** Python 3.11, Django 5.2
- **Database:** PostgreSQL (Render) / SQLite (local development)
- **Media Storage:** Cloudinary CDN
- **Frontend:** HTML5, CSS3, vanilla JavaScript
- **Server:** Gunicorn
- **Static Files:** WhiteNoise
- **Image Processing:** Pillow

## Third-Party Libraries

- Django — web framework
- Pillow — image validation and processing
- gunicorn — production WSGI server
- whitenoise — static file serving in production
- dj-database-url — parses DATABASE_URL environment variable
- psycopg2-binary — PostgreSQL database adapter
- cloudinary — Cloudinary Python SDK
- django-cloudinary-storage — custom storage backend for media uploads

## Models

- **Category** — name, image, is_active, created_at
- **Product** — name, description, price, image, category (ForeignKey), is_active, is_featured, created_at
- **Banner** — title, content, image, is_active, created_at
- **Promotion** — title, content, image, is_active, created_at


## Local Setup

```bash
git clone https://github.com/jibin-jayakumar/Techstore.git
cd Techstore
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS/Linux
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/

## Deployment

Deployed on Render with:
- **Database:** Render PostgreSQL (free tier)
- **Media Storage:** Cloudinary CDN
- **Web Server:** Gunicorn
- **Static Files:** WhiteNoise
- **Superuser:** Auto-created on every deploy via `python manage.py create_admin`

**Note:** The site runs on Render's free tier, so it sleeps after 15 minutes of inactivity. The first request after a period of inactivity may take up to 30 seconds to load.

## License

Educational project. Not for commercial use.
