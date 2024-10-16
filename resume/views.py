from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.

def resume_view(request:HttpRequest):

    context = {
        'resumes':[
            {'id1':1 , 'name':'django'},
            {'id1':2 , 'name':'python'},
            {'id1':3 , 'name':'mongodb'},
        ]
    }
    return render(request,template_name='resumes/resumes.html',context=context)

def resume_detail_view(request:HttpRequest):
    return render(request, template_name='resumes/detail.html')

