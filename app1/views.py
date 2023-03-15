from django.shortcuts import render

# Create your views here.
def jinja(request):
    d={'a':100,'b':200,'c':500,'name':'SHAIK BABUBASHA','tag':'jinja'}
    return render(request,'jinja.html',context=d)