# StreambaDemoServer
A Django-Rest-Framework API for a Retail Management system

This DRF api provides endpoints for data associated with Retail Management stored in an sqlite3 database. Endpoints provide CRUD operations where appropriate as well as pagination, searching and filtering. 

Instructions(Windows):
Ideally if you have Docker installed navigate to /StreambaDemoServer/TEmPoSapi via PowerShell and run 'docker-compose build'. Once this has finished run 'docker-compose up' to start the api within the docker container. 
-Alternatively 'docker-compose --verbose up' will give you logs should you want them. 

If you have Python configured or are on a mac for example, feel free to try navigating to /StreambaDemoServer/TEmPoSapi/TEmPoSapi and then running 'pip install' to download dependencies followed by 'pipenv shell' and 'python manage.py runserver' to start that way. 

You can then navigate to http://localhost:8000/api/v1/ and login with username 'streamba' and password 'streambapassword' to explore the API via browser. For the sake of this demo I have included the sqlite3 database so that there's some data already there. 

Feel free to email me if you have any problems!
