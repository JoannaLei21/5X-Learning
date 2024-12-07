from django.shortcuts import render, redirect, get_object_or_404
from .forms import MembersForm
from .models import Members

# Create your views here.
def index(request):
    if request.POST:
        form = MembersForm(request.POST)
        form.save()
        
        return redirect ("members:index")

    members = Members.objects.all()
    return render(request,"index.html", { "members":members})

def new(request):
    return render (request, "new.html")

def file(request, id):
    members = get_object_or_404(Members, id= id)
    
    if request.POST:
        form = MembersForm(request.POST )
        form.save()
        
        return redirect ("members:index")

    members = Members.objects.all()
    return redirect(request, "file.html")
