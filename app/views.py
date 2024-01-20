from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def djforms(request):
    ENFO=NameForm()                  #ENFO=empty name form object
    d={'ENFO':ENFO}
    if request.method=='POST':
        print('here')
        NFDO=NameForm(request.POST)     #NFDO=name form data object
        if NFDO.is_valid():
            return HttpResponse(str(NFDO.cleaned_data))
        else:
            return HttpResponse('data is not valid')
    return render(request,'djforms.html',d)