from django.shortcuts import render
from django.http import HttpResponseRedirect
from orphanages.models import Orphanage,Oldagehome

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def orphanages(request):
    orp = Orphanage.objects.all()
    return render(request,"orphanage.html",{'orphanages':orp})

def orphanage(request,url):
    orp = Orphanage.objects.filter(url=url).first()
    if not orp:
        return HttpResponseRedirect("/orphanages")
    return render(request,"single.html",{'orphanage':orp})

def oldagehomes(request):
    orp = Oldagehome.objects.all()
    return render(request,"oldagehomes.html",{'oldagehomes':orp})

def oldagehome(request,url):
    orp = Oldagehome.objects.filter(url=url).first()
    if not orp:
        return HttpResponseRedirect("/oldagehomes")
    return render(request,"oldagehome.html",{'oldagehome':orp})
# Create your views here.
