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
			skills=form.cleaned_data['skills']
			mobile=form.cleaned_data['mobile']
			address=form.cleaned_data['address']
			experience=form.cleaned_data['experience']
			#to add more go to : forms.py
			print(name,email)
	return render(request,'info.html',{'form':form})
