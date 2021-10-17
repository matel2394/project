from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def footer(request):
    return render(request,'footer.html')
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def comu(request):
    return render(request,'comu.html')
def 약관(request):
    return render(request,'약관.html')
def 고객센터(request):
    return render(request,'고객센터.html')
def write(request):
    return render(request,'write.html')
def tetrible(request):
    return render(request,'tetrible.html')
def write1(request):
    return render(request,'write1.html')
def news(request):
    return render(request,'news.html')
def onlien(request):
    return render(request,'online.html')
def event(request):
    return render(request,'event.html')
def game_event(request):
    return render(request,'game_event.html')
# Create your views here.
