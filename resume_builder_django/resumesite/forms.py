from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit

# class SkillWidget(forms.MultiWidget):
# 	def __init__(self,attrs=None):
# 		super().__init__([
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput(),
# 		],attrs)

# 	def decompress(self,value):
# 		if value:
# 			return value.split(' ')
# 		return(['','','','','','',''])

# class SkillsField(forms.MultiValueField):
# 	widget=SkillWidget
# 	def __init__(self,*args,**kwargs):
# 		fields=(forms.CharField(),
# 			forms.CharField(),
# 			forms.CharField(),
# 			forms.CharField(required=False),
# 			forms.CharField(required=False),
# 			forms.CharField(required=False),
# 			forms.CharField(required=False),
# 			)
# 		super().__init__(fields,*args,**kwargs)

# 	def compress(self,data_list):
# 		return f'{data_list[0]} {data_list[1]} {data_list[2]} {data_list[3]} {data_list[4]} {data_list[5]} {data_list[6]}'


# class ExpWidget(forms.MultiWidget):
# 	def __init__(self,attrs=None):
# 		super().__init__([
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput()#,
# 		],attrs)

# 	def decompress(self,value):
# 		if value:
# 			return value.split(' ')
# 		return(['','',''])

# class ExpField(forms.MultiValueField):
# 	widget=ExpWidget
# 	def __init__(self,*args,**kwargs):
# 		fields=(forms.CharField(),#validators can be added
# 			forms.CharField(),
# 			forms.CharField(),
# 			)
# 		super().__init__(fields,*args,**kwargs)

# 	def compress(self,data_list):
# 		return f'{data_list[0]} {data_list[1]} {data_list[2]}'

# class EduWidget(forms.MultiWidget):
# 	def __init__(self,attrs=None):
# 		super().__init__([
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput()#,
# 		],attrs)

# 	def decompress(self,value):
# 		if value:
# 			return value.split(' ')
# 		return(['','',''])

# class EduField(forms.MultiValueField):
# 	widget=EduWidget
# 	def __init__(self,*args,**kwargs):
# 		fields=(forms.CharField(),#validators can be added
# 			forms.CharField(),
# 			forms.CharField(),
# 			)
# 		super().__init__(fields,*args,**kwargs)

# 	def compress(self,data_list):
# 		return f'{data_list[0]} {data_list[1]} {data_list[2]}'


class ContactForm(forms.Form):
	name=forms.CharField()#required=False
	email=forms.EmailField(label='E-Mail')
	mobile=forms.CharField()
	address=forms.CharField()
	skills_1=forms.CharField()
	skills_2=forms.CharField()
	skills_3=forms.CharField()
	skills_4=forms.CharField()

	experience_1_title=forms.CharField()
	experience_1_dur=forms.CharField()
	experience_1_desc=forms.CharField()

	experience_2_title=forms.CharField()
	experience_2_dur=forms.CharField()
	experience_2_desc=forms.CharField()

	education_1=forms.CharField()
	education_1_dur=forms.CharField()
	education1_score=forms.CharField()

	education_2=forms.CharField()
	education_2_dur=forms.CharField()
	education2_score=forms.CharField()

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.helper=FormHelper
		self.helper.form_method="post"
		self.helper.layout=Layout(
			'name',
			'email',
			'mobile',
			'address',
			'skills_1',
			'skills_2',
			'skills_3',
			'skills_4',
			'experience_1_title',
			'experience_1_dur',
			'experience_1_desc',
			'experience_2_title',
			'experience_2_dur',
			'experience_2_desc',
			'education_1',
			'education_1_dur',
			'education1_score',
			'education_2',
			'education_2_dur',
			'education2_score',
			Submit('submit','Submit',css_class="btn-success")
			)