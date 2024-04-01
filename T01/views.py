from django.shortcuts import render,HttpResponse

from serverJSP.settings import COMPANYNAME
from .models import PythonLibs 
from .models import CNC



def main(requests):
    DATA={
    'companyName':COMPANYNAME,
    'pythonLibs': PythonLibs.objects.all(),
    'machines':CNC.objects.all()
}   
    
    return render(requests,f'components/features.html',DATA)

def projects(requests):
    DATA={
    'companyName':COMPANYNAME,
    'pythonLibs': PythonLibs.objects.all(),
    'machines':CNC.objects.all()
}   
    return render(requests,f'components/projects.html',DATA)