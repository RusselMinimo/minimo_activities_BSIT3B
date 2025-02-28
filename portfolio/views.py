from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse
from django.db import models
from .models import PersonalInfo, Skill, Project

# Type hints for model managers
PersonalInfo.objects: models.Manager
Skill.objects: models.Manager
Project.objects: models.Manager

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "pages/portfolio.html")

def home(request: HttpRequest) -> HttpResponse:
    context = {
        'personal_info': PersonalInfo.objects.first(),
        'skills': {
            'Programming Languages': Skill.objects.filter(category='PROG'),
            'Frameworks': Skill.objects.filter(category='FRAM'),
            'Tools & Technologies': Skill.objects.filter(category='TOOL'),
            'Soft Skills': Skill.objects.filter(category='SOFT'),
        },
        'projects': Project.objects.all(),
    }
    return render(request, 'portfolio/home.html', context)
