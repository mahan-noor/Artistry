from django.shortcuts import render,redirect, get_object_or_404, Http404
from django.contrib.auth.decorators import login_required
from . models import Post, Profile, Comments
from . forms import PostComments, PostImagesForm,PostProfile, UpdateUserProfileForm, NewsLetterForm
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    title = 'Artistic  || World'
    
    return render(request, 'landing/index.html',{'title': title})

def about(request):
    title = 'Artistic  || World'
    form = NewsLetterForm()
    
    return render(request, 'about.html',{'title': title, 'form': form})
    

@login_required(login_url='login')
def photos(request):
    title = 'Artistic  || World'
    posts = Post.objects.all()
    form = NewsLetterForm()
    return render(request,'photo.html',{'posts':posts , 'title':title, 'form':form})
