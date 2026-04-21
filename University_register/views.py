from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def page_view(request):
    return JsonResponse({"text": "Hat geklappt."})
