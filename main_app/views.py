from django.shortcuts import render, redirect
from .forms import ImageModelForm, VideoModelForm, EmailModelForm, UserCreationModelForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        context = {}
        if request.method == "POST":
            if request.FILES:
                if 'image_btn' in request.POST:
                    image_form = ImageModelForm(request.POST, request.FILES)
                    if image_form.is_valid():
                        temp = image_form.save()
                        temp.uploaded_by = request.user
                        temp.save()
                        messages.success(request, 'Image uploaded successfully')
                        return redirect(request.path)
                    else:
                        messages.error(request, 'Invalid file format')
                        return redirect(request.path)
                if 'video_btn' in request.POST:
                    video_form = VideoModelForm(request.POST, request.FILES)
                    if video_form.is_valid():
                        temp = video_form.save()
                        temp.uploaded_by = request.user
                        temp.save()
                        messages.success(request, 'Video uploaded successfully')
                        return redirect(request.path)
                    else:
                        messages.error(request, 'Invalid file format')
                        return redirect(request.path)
            else:
                messages.error(request, 'Please select a file')
        if request.method == 'GET':
            context["image_form"] = ImageModelForm()
            context["video_form"] = VideoModelForm()
            return render(request, 'home.html', context)
    else:
        messages.error(request, 'Please sign in to continue')
        return redirect('signin')


def contact_us(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Please sign in to continue')
        return redirect('signin')
    context = {}
    if request.method == 'POST':
        form = EmailModelForm(request.POST)
        if form.is_valid():
            temp = form.save()
            temp.sent_by = request.user
            temp.save()
            messages.success(request, 'Email sent successfully')
            return redirect(request.path)
    context['form'] = EmailModelForm
    return render(request, 'contact_us.html', context)


def signin(request):
    context = {}
    if request.method == 'POST':
        sign_in_form = AuthenticationForm(request, data=request.POST)
        if sign_in_form.is_valid():
            username = sign_in_form.cleaned_data['username']
            password = sign_in_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('index')
        else:
            for error in sign_in_form.errors:
                messages.error(request, sign_in_form.errors[error])
            return redirect(request.path)
    context['sign_in_form'] = AuthenticationForm()
    return render(request, 'signin.html', context)


def user_logout(request):
    logout(request)
    return redirect('signin')


def register(request):
    context = {}
    if request.method == 'POST':
        registration_form = UserCreationModelForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            messages.success(request, 'User registered successfully')
            return redirect('signin')
        else:
            for error in registration_form.errors:
                messages.error(request, registration_form.errors[error])
            return redirect(request.path)
    context['registration_form'] = UserCreationModelForm()
    return render(request, 'register.html', context)
