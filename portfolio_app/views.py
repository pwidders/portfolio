from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Project

def home(request):
    projects = Project.objects.all()

    paginator = Paginator(projects, 6)
    page = request.GET.get('page')
    paged_projects = paginator.get_page(page)

    context = {
        'projects': paged_projects
    }

    return render(request, 'portfolio_app/home.html', context)