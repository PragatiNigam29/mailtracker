from django.db import models

# Create your models here.
from django.db import models
import uuid

class EmailTrack(models.Model):
    recipient = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    tracking_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    opened = models.BooleanField(default=False)
    opened_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.recipient
    
