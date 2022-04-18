from django.shortcuts import render, redirect, get_object_or_404
from django.http  import HttpResponse
from .models import Profile, Neighbourhood, Business, Post
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm, NewHoodForm, EditHoodForm, NewBizForm, NewPostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form})

@login_required(login_url='/accounts/login/')
def hood(request):
    hoods = Neighbourhood.objects.all()
    return render(request, 'neighbourhoods.html', {"hoods": hoods})


@login_required(login_url='/accounts/login/')
def new_hood(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewHoodForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.admin = current_user.profile

            image.save()

        return redirect('hood')

    else:
        form = NewHoodForm()
    return render(request, 'new_hood.html', {"form": form})


def edit_hood(request):
    current_user = request.user
    if request.method == 'POST':
        form = EditHoodForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            image = form.save(commit=False)
            image.admin = current_user.profile

            image.save()
        return redirect('hood')

    else:
        form = EditHoodForm()
    return render(request, 'edit_hood.html', {'form': form})


def joinhood(request, id):
    hood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = hood
    request.user.profile.save()
    return redirect('hood')


def leavehood(request, id):
    hood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('hood')


@login_required(login_url='/accounts/login/')
def singlehood(request, id):
    hood = Neighbourhood.objects.get(id=id)
    return render(request, 'hood.html', {'hood':hood})

@login_required(login_url='/accounts/login/')
def businesses(request, id):
    business = Business. hood_biz(id=id)
    return render(request, 'business.html', {'business': business})


@login_required(login_url='/accounts/login/')
def newbiz(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewBizForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = current_user

            business.save()

        return redirect('hood')

    else:
        form = NewBizForm()
    return render(request, 'new_business.html', {"form": form})


@login_required(login_url='/accounts/login/')
def posthood(request, id):
    post = Post.hood_post(id=id)
    return render(request, 'hoodpost.html', {'post': post})


@login_required(login_url='/accounts/login/')
def post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user

            post.save()

        return redirect('hood')

    else:
        form = NewPostForm()
    return render(request, 'post.html', {"form": form})