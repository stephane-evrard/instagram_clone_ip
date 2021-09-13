from django.conf import settings
from django.templatetags.static import static
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse, Http404
import datetime as dt
from django.urls import reverse
from .models import Image, Comment, Profile
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import NewImageForm, NewCommentForm, ProfileUpdateForm, RegisterForm
from django.contrib import messages
from .email import send_welcome_email
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index(request):
    date = dt.date.today()
    images = Image.get_images()
    comments = Comment.get_comment()
    
    current_user = request.user 
    if request.method == 'POST':
        form = NewCommentForm(request.POST, auto_id=False)
        img_id = request.POST['image_id']
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = current_user
            image = Image.get_image(img_id)
            comment.image = image
            comment.save()
        return redirect(f'/#{img_id}',)
    else:
        form = NewCommentForm(auto_id=False)

    return render(request, 'index.html', {"date": date, "images":images, "comments":comments, "form": form,})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            form.save()
            send_welcome_email(name, email)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('/')
        
    else:
        form = RegisterForm()
    return render(request, 'registration/registration_form.html', {'form':form})

@login_required(login_url='/accounts/login/')
def search_images(request):
    if 'keyword' in request.GET and request.GET["keyword"]:
        search_term = request.GET.get("keyword")
        searched_images = Image.search_images(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})
