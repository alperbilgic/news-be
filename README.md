# news-be

Instructions given below:

make sure you downloaded python 3.8.10
create an empty folder
open created folder in terminal
python -m venv venv
git clone https://github.com/alperbilgic/news-be.git
cd news-be
python manage.py migrate
python manage.py loaddata initialize.json
python manage.py runserver
