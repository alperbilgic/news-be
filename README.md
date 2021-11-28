# news-be

## Instructions given below:

### make sure you downloaded python 3.8.10
### create an empty folder
### open created folder in terminal

### run given commands in the give order
```
python -m venv venv
.\venv\Scripts\activate
git clone https://github.com/alperbilgic/news-be.git
cd news-be
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata initialize.json
python manage.py runserver
```

## If you want to run backend happy path tests manually. Run below command in terminal when virtual environment is activated
python manage.py test
