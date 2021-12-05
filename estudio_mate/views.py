from django.http import HttpResponse
from .models import Subject, Problem
from django.shortcuts import render
from .funciones import generate_problems
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def index(request):
    subjects = Subject.objects.all()
    context = {"subjects": subjects}
    return render(request, "estudio_mate/index.html", context)

def study(request, subject_id):
    how_many = request.GET["e"] 
    subject = Subject.objects.get(id=subject_id)
    problems = subject.problem_set.all()
    problems = generate_problems(problems, int(how_many))
    context = {"problems": problems, "subject_id": subject_id, "subject": subject}
    return render(request, "estudio_mate/study.html", context)

def problem(request, subject_id, problem_id):
    problem = Problem.objects.get(id=problem_id)
    context = {"subject_id": subject_id, "problem": problem}
    return render(request, "estudio_mate/answer.html", context)

@login_required(login_url='/accounts/login/')
def upload_problem(request, subject_id, problem_id):
    return render(request, "estudio_mate/submit.html")