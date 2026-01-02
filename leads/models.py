from django.db import models

class Lead(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    income = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
