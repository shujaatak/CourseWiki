from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Syllabus(models.Model):
    syllabus_name=models.CharField(max_length=250,unique=True)
    syllabus_path=models.CharField(max_length=250)
    
    syllabus_technologies=models.CharField(max_length=300)
    def get_absolute_url(self):
          
        absolute_url='http://www.wimson.in/syllabus/'+self.syllabus_name
        absolute_url=absolute_url.strip('.txt')
        return absolute_url
    def __repr__(self):
        a=self.syllabus_name
        b=self.syllabus_path
        d=self.syllabus_technologies
        return a
    def _str_(self):
        w=self.syllabus_name
        return w

class Project(models.Model):
	project_name=models.CharField(max_length=250)
	project_description=models.CharField(max_length=2500)
	project_url=models.CharField(max_length=1000)
	project_location=models.CharField(max_length=1000)
	user_id=models.ForeignKey(User)
	first_name=models.CharField(max_length=250,blank=True)
	public_profile=models.CharField(max_length=2000,blank=True)
	
	def _repr_(self):
		p=self.project_name
		return p    


