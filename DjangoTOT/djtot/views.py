from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return HttpResponse("Hi Welcome User")

def abts(r):
	return HttpResponse("<h2 style='background-color:green;color:white;padding:3px;margin-left:230px;margin-right:230px'>This is about page</h2>")

def rc(y,name):
	return HttpResponse("<h2>Hi Welcome {}</h2>".format(name))

def tblpnt(request,y):
	j= ""	
	for m in range(1,11):
		j += "{} x {:02} = {:02}".format(y,m,y*m)+"<br>"
	#print(j)
	return HttpResponse(j)


def rcds(request,name,age):
	return render(request,'fy/usrdt.html',{'n':name,'a':age})


def sample(request):
	return HttpResponse(request,'fy/demo.html')