from django.db import models
from django.conf import settings

class Application(models.Model):
    STATUS_CHOICES = (
        ('applied', 'Applied'),
        ('interview', 'Interview Scheduled'),
        ('rejected', 'Rejected'),
        ('accepted', 'Accepted'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job_name = models.CharField(max_length=255)
    job_category = models.CharField(max_length=255)
    job_skills = models.TextField()  # Store skills as a comma-separated string or JSON
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    application_date = models.DateTimeField(auto_now_add=True)
    feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.job_name} ({self.status})"
