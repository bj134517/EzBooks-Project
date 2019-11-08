from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from users.models import *
	  
class Classes_list(models.Model):
   """Complete list of classes"""
   class_name      = models.CharField(max_length=200)
   major           = models.CharField(max_length = 100)
   class_extension = models.CharField(max_length=200)
   credit          = models.IntegerField(default=25)
   def __str__(self):
      """Returning a string representation of the model"""
      return self.class_name
	 
class Class_schedule(models.Model):
   """Class schedule associated with a user"""
   user_id     = models.OneToOneField(User_profile ,on_delete=models.CASCADE, primary_key=True)
   class1      = models.CharField(max_length = 200,  null = True, blank = True)
   class2      = models.CharField(max_length = 200,  null = True, blank = True)
   class3      = models.CharField(max_length = 200,  null = True, blank = True)
   class4      = models.CharField(max_length = 200,  null = True, blank = True)
   class5      = models.CharField(max_length = 200,  null = True, blank = True)
   class6      = models.CharField(max_length = 200,  null = True, blank = True)
   
   def __str__(self):
     """Returning a string representation of the model"""
     return self.class1+" - "+self.class2+" - "+self.class3+" - "+self.class4+" - "+ self.class5+" - "+self.class6
   
   def create_class(self, major):
     """Create a class schedule linked to a user"""
     query_major = major
     randomn_classes = Classes_list.objects.raw("select id, class_name from main_db.ez_main_classes_list where major = %s order by rand() limit 6", [query_major])
     self.class1 = str(randomn_classes[0])
     self.class2 = str(randomn_classes[1])
     self.class3 = str(randomn_classes[2])
     self.class4 = str(randomn_classes[3])
     self.class5 = str(randomn_classes[4])
     self.class6 = str(randomn_classes[5])
        
     return self
      
