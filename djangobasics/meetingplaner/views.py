from django.shortcuts import render,get_object_or_404
from meetingplaner.models import Meetings, Room

# Create your views here.
def detail(request,id):
    # meeting = get_object_or_404(Meetings, pk=id)
    meeting = Meetings.objects.get(pk = id)
    return render(request, "meetingplaner/detail.html",{"meeting":meeting})

#Please add a new page that shows a list of all room objects.
#The page should be accessible via the URL /rooms.

def rooms_list(request):
    return render(request, "meetingplaner/rooms_list.html",{"rooms":Room.objects.all()})