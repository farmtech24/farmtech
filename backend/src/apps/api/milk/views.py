
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import DailyProduction

@csrf_exempt
def list_daily_production(request):
    """
    View to list all daily milk production records.
    """
    if request.method == 'GET':
        productions = DailyProduction.objects.all()
        data = [{'id': production.id, 'date': production.date, 'milk_production': production.milk_production} for production in productions]
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def add_daily_production(request):
    """
    View to add a new daily milk production record.
    """
    if request.method == 'POST':
        date = request.POST.get('date')
        milk_production = request.POST.get('milk_production')
        # Validate data and create a new record
        try:
            production = DailyProduction.objects.create(date=date, milk_production=milk_production)
            return JsonResponse({'id': production.id, 'date': production.date, 'milk_production': production.milk_production}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def update_daily_production(request, pk):
    """
    View to update an existing daily milk production record.
    """
    try:
        production = DailyProduction.objects.get(pk=pk)
    except DailyProduction.DoesNotExist:
        return JsonResponse({'error': 'Record not found'}, status=404)

    if request.method == 'PUT':
        # Update record with new data
        try:
            date = request.PUT.get('date')
            milk_production = request.PUT.get('milk_production')
            production.date = date
            production.milk_production = milk_production
            production.save()
            return JsonResponse({'id': production.id, 'date': production.date, 'milk_production': production.milk_production})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def delete_daily_production(request, pk):
    """
    View to delete a daily milk production record.
    """
    try:
        production = DailyProduction.objects.get(pk=pk)
    except DailyProduction.DoesNotExist:
        return JsonResponse({'error': 'Record not found'}, status=404)

    if request.method == 'DELETE':
        # Delete record
        production.delete()
        return JsonResponse({'message': 'Record deleted'})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
