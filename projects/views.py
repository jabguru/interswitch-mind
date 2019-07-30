from django.shortcuts import render

# Create your views here.
def create(request):
    return render(request, 'projects/create.html')

def projects(request):
    return render(request, 'projects/projects.html')