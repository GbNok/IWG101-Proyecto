from django.http import HttpResponse
from .models import Subject, Problem
from django.shortcuts import render

def index(request):
    subjects = Subject.objects.all()
    context = {"subjects": subjects}
    return render(request, "estudio_mate/index.html", context)

def study(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    problems = subject.problem_set.all()
    context = {"problems": problems, "subject_id": subject_id, "subject": subject}
    return render(request, "estudio_mate/study.html", context)

def problem(request, subject_id, problem_id):
    subject = Subject.objects.get(id=subject_id) 
    answer = Problem.objects.get(id=problem_id).answer 
    problem = Problem.objects.get(id=problem_id).statement
    context = {"subject_id": subject_id, "answer": answer, "problem": problem, "subject": subject}
    return render(request, "estudio_mate/answer.html", context)
