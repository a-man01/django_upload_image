from django.shortcuts import render, redirect
from .models import UpImage
from .forms import UpImageForm

# Create your views here.

def index(request):
    all_images = UpImage.objects.all()
    context = {
        "images": all_images
    }
    return render(request, 'upload_image/index.html', context)
def upload_image(request):
    if request.method == 'POST':
        form = UpImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UpImageForm()
    context = {'forms': form}
    return render(request, 'upload_image/upload_image.html', context)