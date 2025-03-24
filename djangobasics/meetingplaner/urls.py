from django.urls import path
from meetingplaner import views

urlpatterns = [
    path('<int:id>', views.detail, name="detail"),
    path('rooms', views.rooms_list, name="rooms"),
]
