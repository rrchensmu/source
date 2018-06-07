from django.shortcuts import render

# Create your views here.
def edu_index(request):
    return render(request,'edu/index.html')

def edu_news(request):
    return render(request,'edu/news.html')

def edu_school(request):
    return render(request,'edu/school.html')

def edu_master(request):
    return render(request,'edu/master.html')