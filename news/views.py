from django.shortcuts import render, HttpResponse
from .models import news
from .models import contact as cn
# Create your views here.

def contact(request):
    n=request.GET.get("name")
    e=request.GET.get("email")
    o=request.GET.get("onvan")
    m=request.GET.get("matn")
    if(n!=None):
        cn.objects.create(name=n, email=e, onvan=o, matn=m)
        return HttpResponse("اطلاعات شما ثبت شد")
    return render(request,"news/contact.html")

def home(request):
    l=news.objects.all()
    return render(request,"news/index.html",content_type={"news":l})

def shownews(request,adad):
    l=news.objects.get(id=adad)
    return render(request,"news/show.html",content_type={"khabar":l})

