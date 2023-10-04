from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method=="POST":
        data = request.POST
        dat1= data.dict()
        key=dat1.keys()
        print(key)
    return render(request, 'index.html')