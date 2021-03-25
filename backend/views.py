from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Guest
from .serializers import GuestSerializer

# Create your views here.
@api_view(['GET'])  # function from DRF
def apiOverview(request):
    backend_urls = {
        'List': '/guest-list/',
        'Detail View': '/guest-detail/<str:pk>/',
        'Create': '/guest-create/',
        'Update': '/guest-update/',
        'Delete': '/guest-delete/',
    }
    return Response(backend_urls)

@api_view(['GET'])  # function from DRF
def guestList(request):
    guests = Guest.objects.all()
    # serializing all data many=True
    serializer = GuestSerializer(guests, many=True)
    return Response(serializer.data)


@api_view(['GET'])  # function from DRF
def guestDetail(request, pk):
    guests = Guest.objects.get(id=pk)
    # serializing all data many=True
    serializer = GuestSerializer(guests, many=False)
    return Response(serializer.data)


@api_view(['POST'])  # function from DRF
def guestCreate(request):
    serializer = GuestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])  # function from DRF
def guestUpdate(request, pk):
    guests = Guest.objects.get(id=pk)
    serializer = GuestSerializer(instance=guests, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])  # function from DRF
def guestDelete(request, pk):
    guests = Guest.objects.get(id=pk)
    guests.delete()
    return Response("Deleted !")