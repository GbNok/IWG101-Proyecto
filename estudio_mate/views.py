from .models import Subject, Problem, Solution
from django.shortcuts import render
from .funciones import generate_problems
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


def index(request):
    subjects = Subject.objects.all()
    context = {"subjects": subjects}
    return render(request, "estudio_mate/index.html", context)



def study(request, subject_id):
    how_many = request.GET["e"]
    if how_many == "":
        how_many = 0 
    subject = Subject.objects.get(id=subject_id)
    problems = subject.problem_set.all()
    problems = generate_problems(problems, int(how_many))
    context = {"problems": problems, "subject_id": subject_id, "subject": subject}
    return render(request, "estudio_mate/study.html", context)

def solutions(request, subject_id, problem_id):
    solutions = Solution.objects.all()
    problem = Problem.objects.get(id=problem_id)
    context = {"solutions": solutions, "problem": problem, "subject_id": subject_id}
    return render(request, "estudio_mate/answer.html", context)

@login_required(login_url='/accounts/login/')
def upload_problem(request, subject_id, problem_id):
    if request.method == 'POST':
        try:
            uploaded_file = request.FILES['solution']
            form = Solution(problem=problem_id, solution_file=uploaded_file)
            form.save()
            return HttpResponseRedirect(f'/{subject_id}/problems/{problem_id}/')
        except:
            return HttpResponseRedirect(f'/{subject_id}/problems/{problem_id}/')
    return render(request, 'estudio_mate/submit.html')

@login_required(login_url='/accounts/login/')
def logged_index(request):
    subjects = Subject.objects.all()
    context = {"subjects": subjects}
    return render(request, "estudio_mate/index.html", context)

