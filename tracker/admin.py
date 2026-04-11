from django.contrib import admin
from .models import EmailTrack

class EmailTrackAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'subject', 'tracking_id', 'opened', 'opened_at')

admin.site.register(EmailTrack, EmailTrackAdmin)