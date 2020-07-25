from django.shortcuts import render,HttpResponse,redirect
from django.utils.crypto import get_random_string
# Create your views here.

def index(request):
    request.session['u_id']='empty'
    request.session['count']=0
    return render(request,'index.html')   
def press(request):
    request.session['u_id']=get_random_string(length=14)
    request.session['count']+=1
    return render(request,'index.html')
