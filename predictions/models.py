from django.db import models
from django.contrib.auth.models import User

class PredictionRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    date = models.DateField()
    prediction_result = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
