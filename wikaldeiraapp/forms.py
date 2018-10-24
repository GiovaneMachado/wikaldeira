from django import forms
from .models import Lore

class LoreForm(forms.ModelForm):
	class Meta:
		model = Lore
		fields = ('title', 'text', 'image')
		