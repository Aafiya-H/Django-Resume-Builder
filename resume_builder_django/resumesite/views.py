from django.shortcuts import render
from .forms import ContactForm

def home(request):
	return render(request, 'home.html', {})

def info(request):
	form=ContactForm()
	if request.method == 'POST':
		form=ContactForm(request.POST)
		if form.is_valid():
			name=form.cleaned_data['name']
			email=form.cleaned_data['email']

			skills_1=form.cleaned_data['skills_1']
			skills_2=form.cleaned_data['skills_2']
			skills_3=form.cleaned_data['skills_3']
			skills_4=form.cleaned_data['skills_4']

			mobile=form.cleaned_data['mobile']
			address=form.cleaned_data['address']

			experience_1_title=form.cleaned_data['experience_1_title']
			experience_1_dur=form.cleaned_data['experience_1_dur']
			experience_1_desc=form.cleaned_data['experience_1_desc']

			experience_2_title=form.cleaned_data['experience_2_title']
			experience_2_dur=form.cleaned_data['experience_2_dur']
			experience_2_desc=form.cleaned_data['experience_2_desc']

			education_1=form.cleaned_data['education_1']
			education_1_dur=form.cleaned_data['education_1_dur']
			education1_score=form.cleaned_data['education1_score']

			education_2=form.cleaned_data['education_2']
			education_2_dur=form.cleaned_data['education_2_dur']
			education2_score=form.cleaned_data['education2_score']

			data={'name':name}
			data['email']=email
			data['skills_1']=skills_1
			data['skills_2']=skills_2
			data['skills_3']=skills_3
			data['skills_4']=skills_4

			data['mobile']=mobile
			data['address']=address

			data['experience_1_title']=experience_1_title
			data['experience_1_dur']=experience_1_dur
			data['experience_1_desc']=experience_1_desc

			data['experience_2_title']=experience_2_title
			data['experience_2_dur']=experience_2_dur
			data['experience_2_desc']=experience_2_desc

			data['education_1']=education_1
			data['education_1_dur']=education_1_dur
			data['education1_score']=education1_score

			data['education_2']=education_2
			data['education_2_dur']=education_2_dur
			data['education2_score']=education2_score
			return render(request,'home.html',data)
			#to add more go to : forms.py
			# print(name,email)
	return render(request,'info.html',{'form':form})
