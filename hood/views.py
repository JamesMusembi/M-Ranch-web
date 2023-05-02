from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import *
from hood.forms import *
from hood.models import Profile, Post

from django.contrib import auth


def index(request):
    hood = AnimalsRanch.objects.all().order_by('-id')
    return render(request, 'index.html',{'hood': hood})



def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    
    animalsranch = AnimalsRanch.objects.all()
    
    posts = Post.objects.filter(user_id=current_user.id)
    return render(request, "profile.html", {"profile": profile, ' animalsranch':  animalsranch, "posts": posts,})


@login_required(login_url='/accounts/login/')
def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user_id = user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
            form = UpdateProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():  
                
                profile = form.save(commit=False)
                profile.save()
                return redirect('profile') 
            
    return render(request, 'update_profile.html', {"form":form})


@login_required(login_url="/accounts/login/")



def create_hood(request):
    current_user = request.user
    if request.method == 'POST':
        hood_form = HoodForm(request.POST, request.FILES)
        if hood_form.is_valid():
            hood = hood_form.save(commit=False)
            hood.user = current_user
            hood.save()
        return HttpResponseRedirect('/hood')
    else:
        hood_form = HoodForm()
    context = {'hood_form':hood_form}
    return render(request, 'hood_form.html',context)


def hood(request):
    current_user = request.user
    hood =AnimalsRanch.objects.all().order_by('-id')
    return render(request, 'hoods.html', {'hood': hood,'current_user':current_user})



def single_hood(request,name):
    current_user = request.user
    hood = AnimalsRanch.objects.get(name=name)
    profiles = Profile.objects.filter(animalsranch=hood)
    
    posts = Post.objects.filter(animalsranch=hood)
   
    
    return render(request,'single_hood.html',{'hood': hood,'posts':posts,'current_user':current_user,
                                                            'profiles':profiles})

def join_hood(request,id):
    animalsranch = get_object_or_404(AnimalsRanch, id=id)
    request.user.profile.animalsranch = animalsranch
    request.user.profile.save()
    return redirect('hood')


def leave_hood(request, id):
    hood = get_object_or_404(AnimalsRanch, id=id)
    # request.user.profile.animalsranch = None
    # request.user.profile.save()
    return redirect('hood')    


def create_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = hood
            post.user=current_user
            post.save()
            return redirect('/posts')
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})


def posts(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    posts = Post.objects.all().order_by('-id')
    if profile is None:
        profile = Profile.objects.filter(
            user_id=current_user.id).first() 
        posts = Post.objects.all().order_by('-id')
        
        locations = Location.objects.all()
        animalsranch = AnimalsRanch.objects.all()
        
        
        
        return render(request, "profile.html", {"danger": "Update Profile ", "locations": locations, "animalsranch": animalsranch,  "posts": posts})
    else:
        animalsranch = profile.animalsranch
        posts = Post.objects.all().order_by('-id')
        return render(request, "posts.html", {"posts": posts})



def profiles(request):
    current_user = request.user
    profiles = Profile.objects.all().order_by('-id')
    return render(request, 'profiles.html', {'profiles': profiles,'current_user':current_user})




@login_required(login_url="/accounts/login/")
def businesses(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    

    if profile is None:
        profile = Profile.objects.filter(
            user_id=current_user.id).first()
        
        
        locations = Location.objects.all()
        animalsranch = AnimalsRanch.objects.all()
        
        
        
        return render(request, "profile.html", {"danger": "Update Profile", "locations": locations, "animalsranch": animalsranch, "businesses": businesses})
    else:
        animalsranch = profile.animalsranch
    
        return render(request, "business.html", {"businesses": businesses})
