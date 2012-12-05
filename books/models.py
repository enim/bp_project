from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
	title = models.CharField(max_length=200)

	def __unicode__(self):
		return self.title

class BookStand(models.Model):
	owner = models.ForeignKey(User)
	books = models.ForeignKey(Book)
	register_date = models.DateTimeField('register date')
	vote = models.IntegerField()

