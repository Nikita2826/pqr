from django.shortcuts import render
from .forms import PostForm
from django.http import HttpResponse
# Create your views here.

def create_view(request):
    form = PostForm()
    if request.method == "POST":
        i = request.POST.get("id")
        t = request.POST.get("title")
        c1 = request.POST.get("con")
        cd1 = request.POST.get("cd")
        up1 = request.POST.get("up")
    form = PostForm(id=i,title=t,content=c1,create_at=cd1,update_at=up1)
    if form.is_valid():
        form.save()
        return HttpResponse("DATA")


    return render(request,"app1/create.html",{})