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
            'title':'Survey',
        }
    )

def regsubmit(request):
    try:
        plaintext = request.POST['question1']+request.POST['question2']+request.POST['question3']
        hiddenData = request.POST['hiddenData']
        user = request.POST['userID']
    except (KeyError):

        print(request)
        return render(
        request,
        'kbdyndemo/input.html',
            {
                'title':'Survey error',
            }
        )
    else:
        u = UserInput(userID=user, text=plaintext, typingData=hiddenData, dateOfData=timezone.now())
        u.save()
        return render(
        request,
        'kbdyndemo/thanks.html',
            {
                'title':'Survey Complete',
            }
        )