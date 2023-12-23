from django.shortcuts import render
from .models import Room
# Create your views here.
def rooms(request):
    rooms=Room.objects.all()
    context={"rooms":rooms}
    return render(request,"rooms.html",context)

def room(request,slug):
    context={"slug":slug}
    return render(request,"room.html",context)
