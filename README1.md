git

    git add . 
    git pull origin master
    git commit -m "some commit"
    git push origin master
    git rm -r --cached .
    
    create database booking character set utf8 collate utf8_unicode_ci ;
My Config

create file my.cnf in the project and edit this file
    
    [client]
    database = mydatabase
    user = your_username
    password = password
    default-character-set = utf8

Django

    pip freeze > requirements.txt.
    pip install -r requirements.txt
    python manage.py makemigrations (1 базаны озгорткон сайын аткару зарыл)
    python manage.py migrate (2 базаны озгорткон сайын аткару зарыл)
    python manage.py runserver
    python manage.py startapp cciit (Жаны )


Database
      
    create database booking character set utf8 collate utf8_unicode_ci;

Run the collectstatic management command:

    python manage.py collectstatic

Go through each of your projects apps migration folder and remove everything inside, except the _init_.py file.

    find . -path "/migrations/.py" -not -name "_init_.py" -delete


ÑÑ‚Ð°Ñ‚Ð¸Ñ‡Ð½Ñ‹Ð¹ Ð»Ð¾ÐºÐ°Ð»Ð¸Ð·Ð°Ñ†Ð¸Ñ

    django-admin compilemessages
    django-admin.py makemessages -a

project update

        cd /docker/letsencrypt-docker-nginx/src/booking_prod/backend/booking/
        git pull origin master
        docker-compose up --build -d booking
        
python commands

        docker-compose exec booking python manage.py makemigrations
        docker-compose exec booking python manage.py migrate
        
        python manage.py createsuperuser(админ панелге парол тузу)