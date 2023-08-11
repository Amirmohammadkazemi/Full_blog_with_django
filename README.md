# Full-bblog-with-django
This repository contains the most complete code required for the blog written by Django.
## Install
### Create Virtual Environment:
    
  Unix/MacOS: ```python -m venv .env```
   
  Windows: ```py -m venv myworld```

### Activate virtual environment:
  Unix/MacOS: ```source myworld/bin/activate```
  
  Windows: ```myworld\Scripts\activate.bat```

### Install requirements
```pip install -r requirements.txt```

## Run project
```cd src```
```python3 manage.py migrate```
```python3 manage.py createsuperuser```
```python3 manage.py makemigrations```
```python3 manage.py migrate```
```python3 manage.py runserver:port(default is 8000)```
