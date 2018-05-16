# fsc
Filipino Style Carinderia in Vancouver


## Create virtual environment
    virtualenv -p python3 <env folder>
    
## Activating environment 
    cd <env folder>
    source bin/activate
  
## Installing libraries
    pip install -r requirements.txt  
    
## Running the server
    python manage.py makemigrations --if any changes to model
    python manage.py migrate --if applying migrations
    python manage.py runserver
