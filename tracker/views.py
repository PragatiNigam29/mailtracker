from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import EmailTrack
from django.utils.timezone import now

def track_email(request, tracking_id):
    try:
        email = EmailTrack.objects.get(tracking_id=tracking_id)
        email.opened = True
        email.opened_at = now()
        email.save()
    except:
        pass

    return HttpResponse("Tracked")
