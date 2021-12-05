from .models import Subject, Problem
from django.shortcuts import render
from .funciones import generate_problems
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import ProblemUpload

def handle_uploaded_file(f):
    with open('/static/estudio_mate/images/solution', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


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

def solutions(request, subject_id, problem_id):
    return render(request, "estudio_mate/answer.html", {"answers": ProblemUpload})

@login_required(login_url='/accounts/login/')
def upload_problem(request, subject_id, problem_id):
    if request.method == 'POST':
        form = ProblemUpload(request.POST, request.FILES, subject_id, problem_id)
        if form.is_valid():
            form.save()
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/subject_id/problems/problem_id/')
    else:
        form = ProblemUpload()
    return render(request, 'estudio_mate/submit.html', {'form': form})

