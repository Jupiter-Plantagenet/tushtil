from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse

@api_view(["GET"])
def home(request, *args, **kwargs):
  header = {"Access-Control-Allow-Origin":"*"}
  data = {
    "slackUsername":"theStormGod",
    "backend":True,
    "age": 21,
    "bio":"Engineering undergrad at the Federal University of Technology, Owerri"
  }
  return JsonResponse(data, headers=header)


