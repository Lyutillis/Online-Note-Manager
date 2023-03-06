from django.contrib import admin
from .models import Note
from django import forms

class NoteAdminForm(forms.ModelForm):
	class Meta:
		model = Note
		widgets = {
			'body': forms.Textarea(attrs={'rows':4, 'cols':40}),
			}
		fields = '__all__'

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin) :
	form=NoteAdminForm
	list_display=['id', 'title', 'body', 'user']
	list_filter=['id', 'title', 'user']
