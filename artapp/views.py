from django.shortcuts import render,redirect, get_object_or_404, Http404

# Create your views here.

def home(request):
    title = 'Artistic  || World'
    
    return render(request, 'landing/index.html',{'title': title})