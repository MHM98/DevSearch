from django.core import paginator
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Tag, project as pj
from .forms import ProjectForm ,ReviewForm
from .utils import searchProject ,paginateProjects


# Create your views here.


def projects(request):
    projects , search_query= searchProject(request)
    custom_range , projects=paginateProjects(request,projects,6)
       
    content={'projects':projects, 'search_query':search_query,'custom_range':custom_range}
    return render(request,'projects/projects.html',content)

def project(request,pk):
    projectObj=pj.objects.get(id=pk)
    form=ReviewForm()
    if(request.method=='POST'):
        form=ReviewForm(request.POST)
        review=form.save(commit=False)
        review.project=projectObj
        review.owner=request.user.profile
        review.save()
        projectObj.getVoteCount 
        messages.success(request,'Your review was successfully submitted!')
        return redirect('project',pk=projectObj.id)

    return render(request,'projects/single-project.html',{'project':projectObj,'form':form})

@login_required(login_url='login')
def createProject(request):
    profile=request.user.profile # this is for saving project.owner in database
    if request.method=='POST':
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.owner=profile
            project.save()
            return redirect('account')
    form=ProjectForm()
    content={'form':form}
    return render(request,'projects/project_form.html',content)

@login_required(login_url='login')
def updateProject(request,pk):
     #project=pj.objects.get(id=pk)  # this work but it has a poor security  we should use below method
     #form=ProjectForm(instance=project)
     profile=request.user.profile
     project=profile.project_set.get(id=pk)
     #
     form=ProjectForm(instance=project)
     if request.method=='POST':
         form=ProjectForm(request.POST,request.FILES,instance=project)
         if form.is_valid():
             form.save()
             return redirect('account')
     content={'form':form}
     return render(request,'projects/project_form.html',content)

@login_required(login_url='login')
def deleteProject(request,pk):
    #project=pj.objects.get(id=pk)  # this work but it has a poor security  we should use below method
    profile=request.user.profile
    project=profile.project_set.get(id=pk)
    #
    if request.method=="POST":
        project.delete()
        return redirect('account')
    content={'object':project}
    return render(request,'delete_template.html',content)