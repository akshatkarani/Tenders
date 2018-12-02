### Various files

- **advert**: This folder contains business listings.
- **post**: This folder contains tenders.
- **tendera**: This folder contains metadata and django files.
- **users**: This folder contains information about users.
- **media**: This folder contains all the documents uploaded.
- settings.py is the central configuration for all the settings in the project including the list of allowed hosts, email backend, database involved etc.
- A model is a class that represents table or collection in our DB, and where every attribute of the class is a field of the table or collection. Models are defined in the app/models.py where app can be ["advert", "post", "users"].
- Django has his own way for URL mapping and it's done by editing your project url.py file (myproject/url.py), further the truncated urls are in the specific apps in the file urls.py.
- Django class and the class attributes will be the form fields which can be found in forms.py in all the apps.
- Django offers a set of classes for generic views in django.views.generic, and every generic view is one of those classes or a class that inherits from one of them. Further custom views are stored in views.py in all the apps.
- Django makes it possible to separate python and HTML, the python goes in views and HTML goes in templates. All the templates are stored in the templates folder in the specific apps.
- Migrations store the database queries in all the apps.

### Code organization is as follows:
```
.
├── advert
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   ├── models.py
│   ├── static
│   │   ├── advert
│   │   │   └── main.css
│   │   └── tendera.png
│   ├── templates
│   │   ├── advert
│   │   │   ├── about.html
│   │   │   ├── advert_confirm_delete.html
│   │   │   ├── advert_detail.html
│   │   │   ├── advert_form.html
│   │   │   └── home.html
│   │   └── advert_confirm_delete.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── media
│   ├── business_pics
│   ├── review_docs
│   ├── tender_docs
│   └── user_pics
├── post
│   ├── __init__.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   ├── models.py
│   ├── static
│   │   ├── Tendera.html
│   │   ├── Tendera_files
│   │   │   ├── AuthenticationService.Authenticate
│   │   │   ├── bg1.jpg
│   │   │   ├── bg3.png
│   │   │   ├── bootstrap.min.css
│   │   │   ├── bootstrap.min.js
│   │   │   ├── common.js
│   │   │   ├── default_business.jpg
│   │   │   ├── jquery.min.js
│   │   │   ├── js
│   │   │   ├── main.css
│   │   │   ├── tendera.png
│   │   │   ├── util.js
│   │   │   └── world-map2.png
│   │   ├── post
│   │   │   └── main.css
│   ├── templates
│   │   └── post
│   │       ├── about.html
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── post_confirm_delete.html
│   │       ├── post_detail.html
│   │       ├── post_form.html
│   │       ├── user_dashboard.html
│   │       ├── user_dashboardads.html
│   │       ├── user_posts.html
│   │       └── welcome.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── tendera
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── users
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── __init__.py
    ├── models.py
    ├── signals.py
    ├── templates
    │   └── users
    │       ├── login.html
    │       ├── logout.html
    │       ├── password_reset.html
    │       ├── password_reset_complete.html
    │       ├── password_reset_confirm.html
    │       ├── password_reset_done.html
    │       ├── profile.html
    │       └── register.html
    ├── tests.py
    ├── urls.py
    └── views.py
```
