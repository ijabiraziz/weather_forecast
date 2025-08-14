import requests
from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import PredictionRequest
from django.conf import settings

class RainPredictionView(LoginRequiredMixin, View):
    template_name = 'predictions/form.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        location = request.POST.get('location')
        date = request.POST.get('date')

        # Call API
        api_key = "211b0522d5e34f40759916ca08fb3cf1"
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units=metric"
        response = requests.get(url).json()

        # Extract rain prediction
        prediction = "No rain"  # default
        for entry in response.get('list', []):
            if entry['dt_txt'].startswith(date) and 'rain' in entry:
                prediction = f"Rain expected: {entry['rain'].get('3h', 0)} mm"

        # Save request
        PredictionRequest.objects.create(
            user=request.user,
            location=location,
            date=date,
            prediction_result=prediction
        )

        return render(request, self.template_name, {
            'location': location,
            'date': date,
            'prediction': prediction
        })
