import sys
import pathlib
import uuid
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import IntegrityError
from User.models import User

# Create your models here.
class Note(models.Model) :

	title=models.CharField(default='No Title', max_length=1000)
	body=models.CharField(default='', max_length=10000)
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	id = models.AutoField(primary_key=True)

# Class methods.

	@staticmethod
	def get_by_id(note_id):
		note = Note.objects.filter(id=note_id).first()
		return note if note else None

	@staticmethod
	def delete_by_id(note_id):
		if Note.get_by_id(note_id) is None:
			return False
		Note.objects.get(id=note_id).delete()
		return True

	@staticmethod
	def create(title=None, body=None, user_id=None):
		note = Note()
		if title:
			note.title = title
		if body:
			note.body = body
		if user_id :
			user=User.objects.filter(id=user_id).first()
			note.user=user	
		else :
			return False
		note.save()
		return note

	def update(self, title=None, body=None):
		if title is not None:
			self.title = title

		if body is not None:
			self.body = body

		self.save()

	@staticmethod
	def get_all():
		return list(Note.objects.all())