from django.shortcuts import redirect, render

def home(request):
    #return render(request,'home.html')    
    return redirect("cars:list")

