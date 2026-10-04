# TechStore — Django E-Commerce Website

A dynamic e-commerce website built with Django, inspired by the Apple Store experience.

## Live Demo

- **Website:** *(update after deploy)*
- **Admin Panel:** *(update after deploy)*

## Credentials

### Admin
- Username: `admin`
- Password: *(update)*

### Test User
- Username: `testuser`
- Password: *(update)*

## Features

- **Dynamic Homepage** — hero banners, featured products, categories, promotions, footer — all database-driven
- **Product Catalog** — browse all products, filter by category, individual detail pages
- **Admin Panel** — full CRUD for Products, Categories, Banners, Promotions, and Users via Django Admin
- **User Authentication** — registration, login, logout, protected profile page using Django's built-in session auth
- **Responsive Design** — mobile-friendly layout using CSS Grid and Flexbox

## Tech Stack

- **Backend:** Python 3.11, Django 5.2
- **Database:** SQLite
- **Frontend:** HTML5, CSS3, vanilla JavaScript
- **Server:** Gunicorn
- **Static Files:** WhiteNoise
- **Image Handling:** Pillow

## Third-Party Libraries

- Django — web framework
- Pillow — image uploads
- gunicorn — production WSGI server
- whitenoise — static file serving in production

## Local Setup

```bash
git clone https://github.com/jibin-jayakumar/Techstore.git
cd Techstore
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver