from django.shortcuts import render

# Create your views here.
def edu_index(request):
    return render(request,'edu/index.html')
def edu_news(request):
    return render(request,'edu/news.html')