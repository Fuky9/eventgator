from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, blank=True, null=True)
    event_date = models.DateField()
    event_time = models.TimeField()


class UserEventRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name="registrations", on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, db_index=True)
    # With related name "comments" it is possible to call all user comments with User.comments.all
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="comments")

    class Meta:
        ordering = ["created_at"]
