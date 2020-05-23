from django.db import models

class CourseMember(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=200)
	phone = models.CharField(max_length=50)
	course = models.CharField(max_length=20)

class Contribute(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=200)
	phone = models.CharField(max_length=50)
	message = models.CharField(max_length=300)