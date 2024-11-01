from rest_framework import serializers
from .models import person

#we can even create modelSeriliser
#Serializers: allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.
#In Django, forms are used to handle user input, validate data, and render HTML form elements. They provide a way to interact with the user, collect information, and process that information within a Django application. Forms in Django can be created either as Django Forms (based on django.forms) or Model Forms (based on django.forms.ModelForm).
#QuerySet is a collection of database queries to retrieve objects from your database. I
#create your models here.

# it is serilizer class
class peopleserilizer(serializers.ModelSerializer):

    #In order to know which model to serilisize we use the meta class
    class Meta:
        # in this we will add model which will automatically knows which model to serilise
    #make sure to use the same nameing convention for identifiers    
        model = person
        #in order to sepcify which field to serilise we have 3 types
        fields = ["name" , 'age' , 'height']
        #2 type
        #fields = "__all__"
        #3 type
        #exclude = ['age']