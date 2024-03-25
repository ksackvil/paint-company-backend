from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Inventory
from .serializers import InventorySerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def list_inventory(request) -> Response:
    inventory = Inventory.objects.all()
    serializer = InventorySerializer(inventory, many=True)
    return Response(serializer.data)


@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def update_inventory_item(request, id) -> Response:
    item = get_object_or_404(Inventory, id=id)

    # Attempt to partially update given item
    serializer = InventorySerializer(item, data=request.data, partial=True)
    if not serializer.is_valid():
        # request.data is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer.save()
    return Response(serializer.data)
