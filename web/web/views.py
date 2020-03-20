from django.http import HttpResponse
from django.shortcuts import render

from .form import ContactForm



def home_page(request):
	my_title = "Welcome to my game."
	return render(request,"game.html", {"title": my_title})



def contact_page(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		form = ContactForm()
	context = {
	"title": "Contact us",
	"form": form

	}
	return render(request,"form.html", context)



def about_page(request):
	return render(request,"contact.html", {"title": "About me"})