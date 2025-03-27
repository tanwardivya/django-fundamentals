from django.shortcuts import render
from django.http import HttpResponse
from meetingplaner.models import Meetings

# Create your views here.
def welcome(request):
    if request.user.is_authenticated:
        context= {"meetings": Meetings.objects.all()}
    else:
        context = {}
    return render(request,"meetings/welcome.html",
                  context)

def about(request):
    return HttpResponse("I am Divya and I am learning Django Fundamentals from PluralSight.")
