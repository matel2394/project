from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def footer(request):
    return render(request,'footer.html')
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
# Create your views here.
