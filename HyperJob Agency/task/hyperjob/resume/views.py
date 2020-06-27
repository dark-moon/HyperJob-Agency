from django.shortcuts import render
from django.views import View
from .models import Resume
from django.shortcuts import redirect


class ResumeView(View):
    def get(self, request, *args, **kwargs):
        resumes = Resume.objects.all()
        return render(request, 'resume/resume.html', context={'resumes': resumes})


class CreateResumeView(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            Resume.objects.create(author=request.user, description=request.POST.get('description'))
            return redirect('/home')
