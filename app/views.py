from django.shortcuts import render
from django.http import HttpResponse
from app import forms
# Create your views here.
from app import utilities

def home(request):
    if request.method=="POST":
        form=forms.SampleForm(request.POST, request.FILES)
        if form.is_valid()== False:
            return render(request,"app/sample.html",{'form':form})
        else:
            data=form.cleaned_data
            profile_pic=data['profile_pic']
            utilities.store_image(profile_pic)
            print(form.cleaned_data)
    form=forms.SampleForm()
    return render(request,"app/sample.html",{'form':form})