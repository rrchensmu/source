"""atms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from edu import views as edu_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    url(r'^edu/index.html', edu_views.edu_index),
    
    url(r'^edu/news.html', edu_views.edu_news),#学校资讯
    
    url(r'^edu/school.html', edu_views.edu_school),#学校概况
    url(r'^edu/master.html', edu_views.edu_master),       
    url(r'^edu/honour.html', edu_views.edu_honour),
    url(r'^edu/teacher.html', edu_views.edu_teacher),
    url(r'^edu/schoolimg.html', edu_views.edu_schoolimg),
    url(r'^edu/schoolfellow.html', edu_views.edu_schoolfellow),
    
    url(r'^edu/education.html', edu_views.edu_education),
    
    url(r'^edu/', edu_views.edu_index),
]
