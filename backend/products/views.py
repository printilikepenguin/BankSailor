from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_list_or_404, get_object_or_404


@api_view(['GET'])
def deposit_list(request):
    if request.method == 'POST':
        pass

def saving_list(request):
    pass