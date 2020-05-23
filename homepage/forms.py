from django import forms
from .models import CourseMember
from .models import Contribute

class CourseMemberForm(forms.ModelForm):
	class Meta:
		model = CourseMember
		fields = ['name','email','phone','course']

class ContributeForm(forms.ModelForm):
	class Meta:
		model = Contribute
		fields = ['name','email','phone','message']