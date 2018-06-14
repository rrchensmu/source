from django.shortcuts import render

# Create your views here.
def edu_index(request):
    return render(request,'edu/index.html')

def edu_news(request):
    return render(request,'edu/news.html')

def edu_school(request):
    return render(request,'edu/school/school.html')

def edu_master(request):
    return render(request,'edu/school/master.html')

def edu_teacher(request):
    return render(request,'edu/school/teacher.html')

def edu_honour(request):
    return render(request,'edu/school/honour.html')

def edu_schoolimg(request):
    return render(request,'edu/school/schoolimg.html')

def edu_schoolfellow(request):
    return render(request,'edu/school/schoolfellow.html')

def edu_education(request):
    return render(request,'edu/education/education.html')