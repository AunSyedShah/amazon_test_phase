from django.shortcuts import render, redirect
from .forms import SignInForm, ImageModelForm, VideoModelForm, EmailModelForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


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
        sign_in_form = SignInForm(request.POST)
        if sign_in_form.is_valid():
            username = sign_in_form.cleaned_data['username']
            password = sign_in_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect(request.path)
    context['sign_in_form'] = SignInForm()
    return render(request, 'signin.html', context)


def user_logout(request):
    logout(request)
    return redirect('signin')
