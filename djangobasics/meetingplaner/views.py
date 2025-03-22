from django.shortcuts import render,get_object_or_404
from meetingplaner.models import Meetings

# Create your views here.
def detail(request,id):
    # meeting = get_object_or_404(Meetings, pk=id)
    meeting = Meetings.objects.get(pk = id)
    return render(request, "meetingplaner/detail.html",{"meeting":meeting})