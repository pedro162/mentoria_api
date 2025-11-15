from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def hello(request):
    """
    Um endpoint simples para teste.
    ---
    responses:
      200:
        description: Retorno simples
    """
    
    return Response({"message": "Hello from Django REST API!"})

