from django import forms
from django.db import models
from django.forms import ModelForm

class Wishlist(models.Model):	
	name = models.CharField(max_length=200)
	wish1 = models.CharField(max_length=200)
	wish2 = models.CharField(max_length=200)
	wish3 = models.CharField(max_length=200)
	wish4 = models.CharField(max_length=200)
	wish5 = models.CharField(max_length=200)

class WishlistForm(ModelForm):
	class Meta:
		model = Wishlist
		widgets = {
            'name': forms.TextInput(attrs={'class':'title'}),
			'wish1': forms.TextInput(attrs={'class':'text'}),
			'wish2': forms.TextInput(attrs={'class':'text'}),
			'wish3': forms.TextInput(attrs={'class':'text'}),
			'wish4': forms.TextInput(attrs={'class':'text'}),
			'wish5': forms.TextInput(attrs={'class':'text'})
        }