from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.
def index(request):
    insert_me={"insertme":"Hello Everyone"}
    return render(request,"first_app/index.html",context=insert_me)

def form_name_view(request):
    form=forms.FormName()
    return render(request,"first_app/form_page.html",{"form":form})
