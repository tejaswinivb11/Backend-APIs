from django.db import models


#model should be a class 
class person(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    height = models.IntegerField(default=0)
    weight=models.IntegerField(default=0)#when ever we create a new filed in the later stages of devleopment we need to have default vale set
#remark: the migrations probelem can be handeled using the migration folder 
