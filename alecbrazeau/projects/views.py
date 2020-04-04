from django.shortcuts import render
from django.views import generic
from .models import Project


class ProjectsList(generic.ListView):
    queryset = Project.objects.order_by('-created_on')
    template_name = 'index.html'


class ProjectDetail(generic.DetailView):
    model = Project
    template_name = 'project_detail.html'


# def index(request):
#     return render(request, 'projects/index.html')
