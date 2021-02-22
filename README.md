# Django-Rest-API

>This Rest API made with the django rest framework, it can be used to deploy scikit learn models saved with the Pickle module.


## Restful API:

* Translator between two machines over a web service.
* API that acts on a restful web service
* Rest apis are programmed so that a server can recieve information from applications such as desktop apps, ios or android apps
* These apis return JSON files which can be interpreted by all machines.

## Django rest framework:

* Web browseable API, huge usability win
* Built in Auth
* Built in serialization

### STEPS:

```
django-admin startproject API
python manage.py makemigrations
python manage.py migrate
python manage.py startapp api_basic
python manage.py createsuperuser 
```
Then, create a model and add 'rest_framework', 'api_basic' to INSTALLED_APPS, make migrations and migrate register the model with the admin.

## Serializer

* This is the process of converting your output into JSON to be the ouput of the API
* This works like regular django forms, theres a lot of repitition as you need to specify all of the fields.

### STEPS

convert model with serializers in serializers.py

```
from api_basic.models import Article
from api_basic.serializers import ArticleSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
```

## Model Serializer

This works like django model forms, theres less repition as the serializer inherits from the model
