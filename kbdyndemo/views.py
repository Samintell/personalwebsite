from django.shortcuts import render
from django.http import HttpRequest
from .models import UserInput
from django.utils import timezone

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

def regsubmit(request):
    try:
        plaintext = request.POST['plaintext']
        hiddenData = request.POST['hiddenData']
        user = request.POST['userID']
    except (KeyError):
        return render(
        request,
        'kbdyndemo/input.html',
            {
            
            }
        )
    else:
        u = UserInput(userID=user, text=plaintext, typingData=hiddenData, dateOfData=timezone.now())
        u.save()