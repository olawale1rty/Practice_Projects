from django.http import HttpResponse
from django.shortcuts import render



def home_page(request):
	my_title = "Welcome to my game."
	return render(request,"game.html", {"title": my_title})



def contact_page(request):
	return render(request,"contact.html", {"title": "Contact me"})



def about_page(request):
	return render(request,"game.html", {"title": "About me"})