from django.shortcuts import render, redirect
from random import *

def home(request):
	return render(request,"home.html")

def show(request):
	if request.GET.get("length"):
		length=int(request.GET.get("length"))
		pw=""
		text="abcdefghijklmnopqrstuvwxyz"
		if request.GET.get("uc"):
			text=text + text.upper()
		if request.GET.get("di"):
			text=text + "0123456789"
		for i in range(length):
			r = randrange(len(text))
			pw = pw + text[r]
		msg="password is " + str(pw)
		return render(request,"show.html", {"msg":msg})
	else:
		return redirect("home")
			

