from django.shortcuts import render
from django.http import JsonResponse
from .models import Reservoir

def map_view(request):
    return render(request, 'mapapp/map.html')

def reservoir_search(request):
    query = request.GET.get("q", "")
    results = []

    if query:
        qs = Reservoir.objects.filter(name__icontains=query)[:10]
        results = [
            {
                "name": r.name,
                "lat": r.latitude,
                "lon": r.longitude,
            }
            for r in qs
        ]

    return JsonResponse(results, safe=False)
