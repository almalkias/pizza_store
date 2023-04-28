from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .forms import Pizza_Form

# Create your views here.
def index(request):
    return render(request, 'app_1/home.html')


# display Forms Of select Type of Pizza_Forms
def Type_of_Pizza(request):
    form=Pizza_Form()
    context = {
    "form": form
    }
    return render(request, 'app_1\select_pizza.html' , context)

def Type_of_Pizza(request):
    form = Pizza_Form()
    if request.method == "POST":
        form = Pizza_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("app_1/home.html")
    context = {
        "form": form,
    }
    return render(request, 'app_1\select_pizza.html', context)
