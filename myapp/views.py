from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def portfolio(request):
    return render(request,'portfolio-details.html')
def blog(request):
    return render(request,'blog-single.html')