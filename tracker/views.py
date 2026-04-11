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
    from django.core.mail import send_mail
from django.http import HttpResponse
from .models import EmailTrackModel
import uuid

def send_email(request):
    tracking_id = uuid.uuid4()

    email = EmailTrackModel.objects.create(
        recipient="test@gmail.com",
        subject="Test Email",
        message="Hello from tracker",
        tracking_id=tracking_id
    )

    tracking_link = f"http://127.0.0.1:8000/tracker/track/{tracking_id}/"

    send_mail(
        subject=email.subject,
        message=f"Open this link to track: {tracking_link}",
        from_email="yourgmail@gmail.com",
        recipient_list=[email.recipient],
        fail_silently=False,
    )

    return HttpResponse("Email sent successfully 🚀")
