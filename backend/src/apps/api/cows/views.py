from django.shortcuts import render
from django.http import JsonResponse
from .models import Cow
from .forms import CowForm

def cow_list(request):
    cows = Cow.objects.all()
    data = [{'id': cow.id, 'nombre': cow.nombre, 'arete': cow.arete, 'nacimiento': cow.nacimiento,
             'numero_partos': cow.numero_partos, 'lote': cow.lote, 'codigo_unico': cow.codigo_unico,
             'category': cow.category, 'photo_url': cow.photo.url if cow.photo else None} for cow in cows]
    return JsonResponse(data, safe=False)

def upload_cow_photo(request):
    if request.method == 'POST':
        form = CowForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Cow photo uploaded successfully'}, status=201)
    else:
        form = CowForm()
    return render(request, 'cows/upload_cow_photo.html', {'form': form})

def update_cow(request, cow_id):
    cow = Cow.objects.get(pk=cow_id)
    if request.method == 'POST':
        form = CowForm(request.POST, request.FILES, instance=cow)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Cow information updated successfully'}, status=200)
    else:
        form = CowForm(instance=cow)
    return render(request, 'cows/update_cow.html', {'form': form, 'cow': cow})

def delete_cow(request, cow_id):
    cow = Cow.objects.get(pk=cow_id)
    cow.delete()
    return JsonResponse({'message': 'Cow deleted successfully'}, status=204)

def add_cow(request):
    if request.method == 'POST':
        form = CowForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Cow added successfully'}, status=201)
    else:
        form = CowForm()
    return render(request, 'cows/add_cow.html', {'form': form})
