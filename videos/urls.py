from django.urls import path
from .views import home, life_coach

urlpatterns = [
    path('', home, name='home'),
    path('life-coach/', life_coach, name='life_coach'),
]
