from django import forms
from django.forms.widgets import DateInput
from web_app.models.announcement import Announcement

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content', 'start_time', 'end_time']