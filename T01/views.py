from django.shortcuts import render,HttpResponse

from serverJSP.settings import COMPANYNAME

# Create your views here.
DATA={
    'companyName':COMPANYNAME
}


def main(requests):
    return render(requests,f'components/features.html',DATA)

def projects(requests):
    return render(requests,f'components/projects.html',DATA)