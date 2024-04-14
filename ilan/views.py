from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404
from .models import Ilan
from .forms import IlanForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def index(request):
    il_keyword = request.GET.get("il")
    cinsiyet_keyword = request.GET.get("cinsiyet")
    yas_keyword = request.GET.get("yas")

    if il_keyword or cinsiyet_keyword or yas_keyword:
        ilanlar=Ilan.objects.filter(address__contains = il_keyword,gender__contains = cinsiyet_keyword,age__contains=yas_keyword)
        if ilanlar:                      
            return render(request,"index.html",{"ilanlar":ilanlar})
        else:
            messages.info(request,"İlan mevcut değil !")
            return render(request,"index.html",{"ilanlar":ilanlar})     
    else:
        ilanlar = Ilan.objects.all()

        return render(request,"index.html",{"ilanlar":ilanlar})

def about(request):
    return render(request,"about.html")

@login_required(login_url="user:login")
def dashboard(request):
    ilans = Ilan.objects.filter(advertiser = request.user)

    return render(request,"dashboard.html",{"ilans":ilans})

@login_required(login_url="user:login")
def create(request):
    form = IlanForm(request.POST or None,request.FILES or None)

    if form.is_valid():

        ilan = form.save(commit=False)
        ilan.advertiser = request.user
        ilan.save()
        
        return redirect("ilan:dashboard")

    return render(request,"create.html",{"form":form})

def detail(request,id):
    ilan = get_object_or_404(Ilan,id = id) 

    return render(request,"detail.html",{"ilan":ilan})

@login_required(login_url="user:login")
def update(request,id):
    ilan = get_object_or_404(Ilan,id = id)
    form = IlanForm(request.POST or None,request.FILES or None,instance=ilan)
    if ilan.advertiser == request.user:
        if form.is_valid():
            ilan = form.save(commit=False)
            ilan.advertiser = request.user
            ilan.save()
            
            return redirect("ilan:dashboard")

        return render(request,"update.html",{"form":form})
    else:
        raise Http404


@login_required(login_url="user:login")    
def delete(request,id):
    ilan = get_object_or_404(Ilan,id = id)
    if ilan.advertiser == request.user:
        ilan.delete()

        return redirect("ilan:dashboard")
    else:
        raise Http404