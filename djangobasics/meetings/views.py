from django.shortcuts import render
from django.http import HttpResponse
from meetingplaner.models import Meetings

# Create your views here.
def welcome(request):
    return render(request,"meetings/welcome.html",
        {"num_meetings": Meetings.objects.count()})

def about(request):
    return HttpResponse("I am Divya and I am learning Django Fundamentals from PluralSight.")
