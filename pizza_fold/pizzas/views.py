from django.shortcuts import render


# Create your views here.

def index(request):
    """The home page for meal_plans."""
    return render(request, 'pizzas/index.html')
