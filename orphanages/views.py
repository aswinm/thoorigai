from django.shortcuts import render
from django.http import HttpResponseRedirect
from orphanages.models import Orphanage,Oldagehome
from orphanages.forms import BirthdayForm

def index(request):
    form = BirthdayForm()
    return render(request,"index.html",{'form':form})

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

def birthdaydonation(request):
    if request.method == "POST":
        form = BirthdayForm(request.POST)
        if form.is_valid():
            b = form.save(commit=False)
            b.orphanage = form.cleaned_data["orphanage"]
            b.save()
            return HttpResponseRedirect(b.orphanage.donation_link)
        else:
            return render(request,"index.html",{'form':form})
    else:
        return HttpResponseRedirect("/")

# Create your views here.
