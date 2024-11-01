from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import person
from .serilizer import peopleserilizerp

#view are for handelling requests
#Api views:  ->   API views are the similar to the decotators in python [Decorators are a way to wrap another function or method in order to extend its behavior.]
#            ->REST framework provides an APIView class, which subclasses Django's View class.

#class defination
#class MyModelCreateView(APIView):

#basic api request and reponse
@api_view(['GET','POST', 'PUT' , 'PATCH'])
def index(request):
    #creating json data
    cources = {
        'course_name' : 'python',
        'learn' : ['flask' , 'django'],
        'course_prov' :'tejaswini'
    }
    #inorder to check the type of request
    if request.method == 'GET': 
    #inorder to get the data passed from the url 'search' is the identifier
        print(request.GET.get('serach'))
        return Response(cources)
    elif request.method == 'POST':
        # in order to accept the post data is use, in the form of json 
        data = request.data
        print("*********")
        print(data['name'])
        return Response(cources)
 

#creating an api to work with the model
@api_view(['GET','POST', 'PUT' , 'PATCH'])
def Person(request):
    #getting the data from queryset and coverting it to json
    if request.method == 'GET':
        objs = person.objects.all()   
        #what this returns is the data type of 'quearyset'
        serilizer = peopleserilizer(objs,many=True)#if we have more than one object to return then we need to use this many =true
        return Response(serilizer.data)
    
    #working of post 
    #when the view encounter the post request 
        #it will be send to seruliser using the code spnnite " serilizer = peopleserilizer(data = data)"
        #then the input will ve validated " if serilizer.is_valid():"
        #if correct the instance will be saved in the DB  "serilizer.save()""

    elif request.method == 'POST':
        #for converting the json fromat to queryset
        data = request.data
        #passing the quearyset type data to serilizer and reciving the json type
        serilizer = peopleserilizer(data = data)
        #in order to check weather the given data valid or no
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        else:
            return Response("there wasa error") 
        
    #implementation of put and patch method:
        #the key difference is that about the partial updation of the data
    elif request.method == 'PUT':
        data = request.data
        serilizer=peopleserilizer(data = data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
   #do use upper case
    elif request.method == 'PATCH':
        data = request.data
        obj = person.objects.get(id=data['id'])
        serilizer=peopleserilizer(obj,data = data,partial = True)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)

