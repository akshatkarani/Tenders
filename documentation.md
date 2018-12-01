Code organization is as follows:
.
├── advert
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   ├── admin.cpython-37.pyc
│   │   ├── apps.cpython-37.pyc
│   │   ├── forms.cpython-37.pyc
│   │   ├── models.cpython-37.pyc
│   │   ├── urls.cpython-37.pyc
│   │   └── views.cpython-37.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_auto_20181111_0854.py
│   │   ├── 0003_auto_20181111_0855.py
│   │   ├── 0004_advert_hours.py
│   │   ├── 0005_auto_20181111_0945.py
│   │   ├── 0006_advert_email.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-37.pyc
│   │       ├── 0002_auto_20181103_1607.cpython-37.pyc
│   │       ├── 0002_auto_20181111_0854.cpython-37.pyc
│   │       ├── 0003_auto_20181103_1613.cpython-37.pyc
│   │       ├── 0003_auto_20181111_0855.cpython-37.pyc
│   │       ├── 0004_advert_hours.cpython-37.pyc
│   │       ├── 0004_remove_advert_phone_number.cpython-37.pyc
│   │       ├── 0005_auto_20181111_0945.cpython-37.pyc
│   │       ├── 0006_advert_email.cpython-37.pyc
│   │       └── __init__.cpython-37.pyc
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
│   │   ├── 20181102_201031.jpg
│   │   ├── awesome-profile-pics-300x300-2.jpg
│   │   ├── bg1.jpg
│   │   ├── bg3.png
│   │   ├── bg3_7CsTPpo.png
│   │   ├── default_business.jpg
│   │   ├── default_business_2fvYTys.jpg
│   │   ├── default_business_8mcypfs.jpg
│   │   ├── default_business_PVv4Eli.jpg
│   │   ├── gradient-1761190_960_720.jpg
│   │   └── world-map2.png
│   ├── default_business.jpg
│   ├── default_pic.jpg
│   ├── review_docs
│   │   ├── AXIS_BANK__Statement_for_October_2018_copy.pdf
│   │   ├── Class_Schedule_CSE_III_semester.pdf
│   │   ├── Class_Schedule_CSE_III_semester_wUnLI5c.pdf
│   │   ├── aa.txt
│   │   └── anagrams.txt
│   ├── tender_docs
│   │   ├── 3filter.py
│   │   ├── 877649230.pdf
│   │   ├── CS_211_Assignment_10.pdf
│   │   ├── Coursera_5ZUXP4E7RJ8N.pdf.pdf
│   │   ├── Coursera_5ZUXP4E7RJ8N.pdf_04VdPl2.pdf
│   │   ├── Coursera_EECDLRJVBLWZ.pdf-2.pdf
│   │   ├── Coursera_EECDLRJVBLWZ.pdf-2_JrvyRmO.pdf
│   │   ├── Coursera_WPWTDE2F5JEJ.pdf-2.pdf
│   │   ├── Coursera_WPWTDE2F5JEJ.pdf-2_eZKHQUC.pdf
│   │   ├── Coursera_WPWTDE2F5JEJ.pdf-2_yf6BYB2.pdf
│   │   ├── DetailedTenderDocument.pdf
│   │   ├── a.c
│   │   ├── a.py
│   │   ├── a_6dlb1Q4.py
│   │   ├── aa.html
│   │   └── anagrams.txt
│   └── user_pics
│       ├── 0e559a25-016c-4acd-b28f-714d6676b430.png
│       ├── 0e559a25-016c-4acd-b28f-714d6676b430_e2V1qGQ.png
│       ├── 0e559a25-016c-4acd-b28f-714d6676b430_pfsV0Vg.png
│       ├── Arpit.jpg
│       ├── IMG_20180127_195322_Bokeh.jpg
│       ├── awesome-profile-pics-300x300-2.jpg
│       ├── default.jpg
│       └── logo.png
├── post
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   ├── admin.cpython-37.pyc
│   │   ├── apps.cpython-37.pyc
│   │   ├── forms.cpython-37.pyc
│   │   ├── models.cpython-37.pyc
│   │   ├── urls.cpython-37.pyc
│   │   └── views.cpython-37.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_auto_20181121_1417.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-37.pyc
│   │       ├── 0002_auto_20181110_0928.cpython-37.pyc
│   │       ├── 0002_auto_20181110_1249.cpython-37.pyc
│   │       ├── 0002_auto_20181121_1258.cpython-37.pyc
│   │       ├── 0002_auto_20181121_1304.cpython-37.pyc
│   │       ├── 0002_auto_20181121_1337.cpython-37.pyc
│   │       ├── 0002_auto_20181121_1417.cpython-37.pyc
│   │       ├── 0002_post_item.cpython-37.pyc
│   │       ├── 0002_remove_review_user.cpython-37.pyc
│   │       ├── 0003_post_quantity.cpython-37.pyc
│   │       ├── 0003_review.cpython-37.pyc
│   │       ├── 0003_review_author.cpython-37.pyc
│   │       ├── 0004_auto_20181110_0921.cpython-37.pyc
│   │       ├── 0004_auto_20181121_1222.cpython-37.pyc
│   │       ├── 0005_auto_20181121_1256.cpython-37.pyc
│   │       ├── 0005_remove_post_quantity.cpython-37.pyc
│   │       ├── 0006_post_quantity.cpython-37.pyc
│   │       └── __init__.cpython-37.pyc
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
│   │   ├── bg1.jpg
│   │   ├── bg2.png
│   │   ├── bg3.png
│   │   ├── business-w1.jpg
│   │   ├── post
│   │   │   └── main.css
│   │   ├── tendera.png
│   │   ├── world-map.jpg
│   │   ├── world-map.png
│   │   └── world-map2.png
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
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── __init__.cpython-37.pyc
│   │   ├── settings.cpython-36.pyc
│   │   ├── settings.cpython-37.pyc
│   │   ├── urls.cpython-37.pyc
│   │   └── wsgi.cpython-37.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── users
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-37.pyc
    │   ├── admin.cpython-37.pyc
    │   ├── apps.cpython-37.pyc
    │   ├── forms.cpython-37.pyc
    │   ├── models.cpython-37.pyc
    │   ├── signals.cpython-37.pyc
    │   ├── urls.cpython-37.pyc
    │   └── views.cpython-37.pyc
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── __init__.py
    │   └── __pycache__
    │       ├── 0001_initial.cpython-37.pyc
    │       └── __init__.cpython-37.pyc
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
