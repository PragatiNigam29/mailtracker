from django.urls import path
from . import views

urlpatterns = [
    path('track/<uuid:tracking_id>/', views.track_email, name='track_email'),
    path('send-email/', views.send_email, name='send_email'),
]
