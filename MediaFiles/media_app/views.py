import os
from django.conf import settings
from django.http import FileResponse, Http404, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ImageUploadForm
from .models import UserImage
from django.contrib.auth import logout
from django.contrib.auth import login
from .forms import RegisterForm

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.save(commit=False)
            img.user = request.user
            img.save()
            return redirect('upload')
    else:
        form = ImageUploadForm()

    images = UserImage.objects.filter(user=request.user)
    return render(request, 'upload.html', {'form': form, 'images': images})


@login_required
def protected_image(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)

    # Prevent directory traversal
    if not os.path.abspath(file_path).startswith(settings.MEDIA_ROOT):
        return HttpResponseForbidden("Forbidden")

    if not os.path.exists(file_path):
        raise Http404("File not found")

    return FileResponse(open(file_path, 'rb'), content_type='image/jpeg')

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})