from django.shortcuts import render
from .models import Food

def home(request):
    if request.method == 'POST':
        query = request.POST['query']
        try:
            food = Food.objects.get(name__iexact=query)
            context = {'food': food}
        except Food.DoesNotExist:
            context = {'error': "Food item not found"}
    else:
        context = {'query': 'Enter a valid query'}

    return render(request, 'home.html', context)

