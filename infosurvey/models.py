from django.db import models

class WaitlistEntry(models.Model):
    full_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    user_type = models.CharField(max_length=50)
    urgency = models.CharField(max_length=50)
    security_needs = models.TextField()  # comma-separated values
    budget = models.CharField(max_length=50)
    notes = models.TextField(blank=True)
    consent = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
