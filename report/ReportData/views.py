import json
import os
from django.http import JsonResponse
from django.conf import settings

def report(request):
    # Define the path to your input.json file
    file_path = os.path.join(settings.BASE_DIR, "data", "input.json")
    
    # Read the JSON data
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        return JsonResponse(data)
    except FileNotFoundError:
        return JsonResponse({"error": "File not found"}, status=404)