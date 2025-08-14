````markdown
# Food Recipe Django Web App

A Django-based web application for managing and sharing food recipes, complete with user authentication, CRUD functionality, and image support.

## Features
- User registration, login, and profile management
- Create, read, update, and delete recipes
- Each recipe includes: name, description, price, image
- Media handling for recipe images
- Responsive UI with HTML and CSS (optionally Bootstrap)

## Technologies Used
- **Backend:** Django 5.x
- **Database:** SQLite (default) or PostgreSQL
- **Authentication:** Django's built-in `User` model
- **Media Storage:** Django `MEDIA_URL` and `MEDIA_ROOT`
- **Templates:** Django template language
- **Others:** (e.g. crispy-forms, Bootstrap, etc.)

## Installation & Setup
```bash
git clone https://github.com/davemosh/food-Recipe-in-Django.git
cd food-Recipe-in-Django
python -m venv .venv
.venv/Scripts/activate  # on Windows
pip install -r requirements.txt  # or `pip install django`
python manage.py migrate
python manage.py runserver
````

## Configuration

Update `settings.py`:

```python
DEBUG = True
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"
LOGIN_REDIRECT_URL = 'food:index'
LOGIN_URL = 'login'
```

In `urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  # ... your URL patterns ...
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## Usage

* Navigate to `http://127.0.0.1:8000/food/` to view all recipes.
* Register, log in, and create, edit, or delete recipes.
* Images will display if correctly uploaded and served via `MEDIA_URL`.

## Project Structure

```
food_recipe_app/
├── food/
│   ├── models.py        # Recipe model with name, description, price, image
│   ├── views.py         # CRUD and list/detail views
│   ├── forms.py         # ModelForm for Item
│   └── templates/
│       └── food/
│           ├── index.html
│           ├── details.html
│           ├── item-form.html
│           └── item-delete.html
├── users/
│   └── views.py         # register, login, logout, profile
├── maybe/               # project root
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

## Screenshots

*(Add screenshots here and annotate with descriptions.)*

## Future Improvements

* Add pagination to the recipe list
* Implement recipe categories or tags
* Enhance image upload (e.g., with `ImageField` and `Pillow`)
* Add search or filter functionality
* Deploy to Heroku or PythonAnywhere

## License

This project is licensed under the MIT License. Feel free to use and modify.
