from django.shortcuts import render, redirect
from .forms import SignInForm, ImageModelForm, VideoModelForm, EmailModelForm
from django.contrib import messages


# Create your views here.
def home(request):
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
        form = SignInForm(request.POST)
        if form.is_valid():
            print('form is valid')
            print(form)
            form.save()
            return render(request, 'home.html')
        else:
            context['form'] = form
    context['form'] = SignInForm
    return render(request, 'signin.html', context)
