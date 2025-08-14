from django.urls import path
from .views import RainPredictionView

urlpatterns = [
    path('', RainPredictionView.as_view(), name='predict_rain'),
]
