"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from vacancy.views import WelcomeView
from vacancy.views import VacancyView
from resume.views import ResumeView
from vacancy.views import SignupView
from vacancy.views import LoginCustomView
from vacancy.views import ProfileView
from vacancy.views import CreateVacancyView
from resume.views import CreateResumeView

urlpatterns = [
    path('', WelcomeView.as_view()),
    path('admin/', admin.site.urls),
    path('menu/', WelcomeView.as_view()),
    path('vacancies/', VacancyView.as_view()),
    path('resumes/', ResumeView.as_view()),
    path('signup', SignupView.as_view()),
    path('login', LoginCustomView.as_view()),
    path('signup/', RedirectView.as_view(url='signup')),
    path('login/', RedirectView.as_view(url='login')),
    path('home', ProfileView.as_view()),
    path('vacancy/new', CreateVacancyView.as_view()),
    path('resume/new', CreateResumeView.as_view()),
]
