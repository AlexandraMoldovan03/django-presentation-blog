from django.shortcuts import render
from .models import Video

def home(request):
    return render(request, 'videos/index.html')

def life_coach(request):
    videos = Video.objects.all()
    return render(request, 'videos/life-coach.html', {'videos': videos})
