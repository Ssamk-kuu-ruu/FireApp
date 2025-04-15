from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from django.db.models.functions import ExtractMonth

from django.db.models import Count
from datetime import datetime

class ChartView(ListView):
    template_name = 'chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get_queryset(self, **kwargs):
        pass

    def PieCountbySeverity(request):
        query = '''
        SELECT severity_level, COUNT(*) as count
        FROM fire_incident
        GROUP BY severity_level
        '''
        data = {}
        with connection.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()

        if rows:
            data = {severity: count for severity, count in rows}
        else:
            data = {}

        return JsonResponse(data)


