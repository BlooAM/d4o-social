from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ImageCreateForm


@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_image = cd.save(commit=False)
            new_image.user = request.user
            new_image.save()
            messages.success(request, 'Image has been uploaded.')
            return redirect(new_image.get_absolute_url())
    else:
        form = ImageCreateForm(data=request.GET)

    return render(request, 'images/image/create.html', {'sections': 'images', 'form': form})
