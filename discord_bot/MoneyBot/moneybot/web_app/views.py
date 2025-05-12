from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import items_types
# Create your views here.
def add_type(request):
    data = json.load(request.body)

    item_name = data.get('items')
    new_type = items_types.objects.create(items=item_name)