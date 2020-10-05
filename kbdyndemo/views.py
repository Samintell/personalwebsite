from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def register(request):
    """Renders the input page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'kbdyndemo/input.html',
        {
            
        }
    )