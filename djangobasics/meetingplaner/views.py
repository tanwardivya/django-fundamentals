from django.shortcuts import render,get_object_or_404,redirect
from meetingplaner.models import Meetings, Room
from django.forms import modelform_factory
from django.contrib.auth.decorators import login_required

@login_required
# Create your views here.
def detail(request,id):
    # meeting = get_object_or_404(Meetings, pk=id)
    meeting = Meetings.objects.get(pk = id)
    return render(request, "meetingplaner/detail.html",{"meeting":meeting})

#Please add a new page that shows a list of all room objects.
#The page should be accessible via the URL /rooms.
@login_required
def rooms_list(request):
    rooms = Room.objects.all().order_by('floor_number', 'room_number')  # Ordered list of rooms
    return render(request, "meetingplaner/rooms_list.html",{"rooms":rooms})

MeetingForm = modelform_factory(Meetings,fields = ['title', 'date', 'start_time', 'duration', 'room','participants'])

@login_required
def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
        rooms = Room.objects.all().order_by('floor_number', 'room_number')  # Get ordered rooms
    return render(request, "meetingplaner/new.html",
                  {"form":form,
                   "rooms": rooms})
@login_required
def edit(request,id):
    meeting = get_object_or_404(Meetings,pk=id)
    if request.method == "POST":
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            return redirect("detail", id)
    else:
        form = MeetingForm(instance=meeting)
    return render(request,"meetingplaner/edit.html",{"form":form})
@login_required
def delete(request,id):
    meeting = get_object_or_404(Meetings,pk=id)
    if request.method == "POST":
        meeting.delete()
        return redirect("welcome")
    else:
        return render(request,"meetingplaner/confirm_delete.html",{"meeting":meeting})
    
