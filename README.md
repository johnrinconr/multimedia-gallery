# multimedia-gallery

## Connecting to the database in development mode

1) Open the Heroku dashboard, select "multimedia-gallery" and go to "Resources".

1.1) Click the "Heroku Postgres" under the "Add-ons" tab.
1.2) On the new page select "Settings" and then "View credentials". 

2) Open the root folder of the project, then open "multimediaGallery" and open the "settings.py" file

3) Replace "DATABASES = { ... }" with:

```python
DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': ''
    }
}
```

4) Change NAME, USER, PASSWORD, HOST and PORT with the data displayed on point 1.2 

## Running the app

1. Open a CMD and type "git checkout inception" to change the branch
2. On the root folder use a CMD to execute:

   Windows: "virtualenv env && env\Scripts\activate.bat && pip install -r requirements.txt"

## Before uploading - If you add new modules or libraries

1. In a CMD with the virtual enviroment running. Type "pip freeze"
2. Copy the displayed text and paste it on "requirements.txt"

## Current functionalities

List images: http://127.0.0.1:8000/gallery/
Add image: http://127.0.0.1:8000/gallery/add/
