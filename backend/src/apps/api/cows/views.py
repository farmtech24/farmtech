from django.shortcuts import render, redirect
from .forms import CowForm

def upload_cow_photo(request):
    if request.method == 'POST':
        form = CowForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirigir a una URL
            return redirect('success_url_name')
    else:
        form = CowForm()
    return render(request, 'cows/upload_cow_photo.html', {'form': form})
