from django.shortcuts import render,redirect
from .models import Users
from .forms import Users_forms

# Create your views here.


def home(request):
    if request.method == 'POST' :
        form = Users_forms(request.POST)
        if form.is_valid():
           form.save()
           last_row=Users.objects.all()
        
           return render(request,'index.html',{'form':Users_forms,'latest_row':last_row})
    else:
        form=Users_forms

    return render(request,'index.html',{'form':form})
        




    
    
