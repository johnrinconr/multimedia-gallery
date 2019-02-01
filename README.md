# multimedia-gallery

## Running the app

1. Clone the repository
2. Open a CMD and type "git checkout inception" to change the branch
3. On the root folder use a CMD to execute:

   Windows: "virtualenv env && env\Scripts\activate.bat && pip install -r requirements.txt"

## Before uploading - If you add new modules or libraries

1. In a CMD with the virtual enviroment running. Type "pip freeze"
2. Copy the displayed text and paste it on "requirements.txt"

## Current functionalities

List images: http://127.0.0.1:8000/gallery/
Add image: http://127.0.0.1:8000/gallery/add/
