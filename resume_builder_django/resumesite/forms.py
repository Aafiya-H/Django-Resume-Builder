from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit

class SkillWidget(forms.MultiWidget):
	def __init__(self,attrs=None):
		super().__init__([
			forms.TextInput(),
			forms.TextInput(),
			forms.TextInput(),
			forms.TextInput(),
			forms.TextInput(),
			forms.TextInput(),
			forms.TextInput(),
		],attrs)

	def decompress(self,value):
		if value:
			return value.split(' ')
		return(['','','','','','',''])

class SkillsField(forms.MultiValueField):
	widget=SkillWidget
	def __init__(self,*args,**kwargs):
		fields=(forms.CharField(),
			forms.CharField(),
			forms.CharField(),
			forms.CharField(required=False),
			forms.CharField(required=False),
			forms.CharField(required=False),
			forms.CharField(required=False),
			)
		super().__init__(fields,*args,**kwargs)

	def compress(self,data_list):
		return f'{data_list[0]} {data_list[1]} {data_list[2]} {data_list[3]} {data_list[4]} {data_list[5]} {data_list[6]}'


class ExpWidget(forms.MultiWidget):
	def __init__(self,attrs=None):
		super().__init__([
			forms.TextInput(),
			forms.TextInput(),
			forms.TextInput()#,
		],attrs)

	def decompress(self,value):
		if value:
			return value.split(' ')
		return(['','','','','','',''])

class ExpField(forms.MultiValueField):
	widget=ExpWidget
	def __init__(self,*args,**kwargs):
		fields=(forms.CharField(),#validators can be added
			forms.CharField(),
			forms.CharField(),
			)
		super().__init__(fields,*args,**kwargs)

	def compress(self,data_list):
		return f'{data_list[0]} {data_list[1]} {data_list[2]} {data_list[3]} {data_list[4]} {data_list[5]} {data_list[6]}'

class ContactForm(forms.Form):
	name=forms.CharField()#required=False
	email=forms.EmailField(label='E-Mail')
	mobile=forms.CharField()
	address=forms.CharField()
	skills=SkillsField()
	experience=ExpField()

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.helper=FormHelper
		self.helper.form_method="post"
		self.helper.layout=Layout(
			'name',
			'email',
			'skills',
			'mobile',
			'address',
			'experience',
			Submit('submit','Submit',css_class="btn-success")
			)