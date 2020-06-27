from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from .models import Vacancy
from .customForms import VacancyForm
from .customForms import ResumeForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        # return render(request, './menu.html')
        return render(request, 'vacancy/menu.html')


class VacancyView(View):
    def get(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.all()
        return render(request, 'vacancy/vacancy.html', context={'vacancies': vacancies})


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'vacancy/signup.html'


class LoginCustomView(LoginView):
    form = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'vacancy/login.html'


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        vacancy_form = VacancyForm()
        resume_form = ResumeForm()
        return render(request, 'vacancy/user_profile.html', context={
            'vacancy_form': vacancy_form,
            'resume_form': resume_form
        })


class CreateVacancyView(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            Vacancy.objects.create(
                author=request.user,
                description=request.POST.get('description')
            )
            return redirect('/home')
        else:
            raise PermissionDenied()


class CreateResumeView(View):
    def post(self, request, *args, **kwargs):
        return HttpResponse(f"<h1>{request.user}: {request.POST.get('description')}</h1>")
