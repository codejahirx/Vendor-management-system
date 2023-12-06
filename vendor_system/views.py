from django.shortcuts import render
from rest_framework.response import Response
from django.utils import timezone
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework import status
from vendor_system.models import Vendor, PurchaseOrder
from vendor_system.serializers import AcknowledgeSerializer, PerformanceSerializer, PurchaseOrderSerializer, VendorSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


def home_page(request):
    return render(request, 'home.html')

# List all vendors or create a new vendor


class VendorListCreate(ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        if not queryset.exists():

            return Response({"message": "No vendors found"}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data, status=status.HTTP_200_OK)

# Retrieve details or update a specific vendor


class VendorRetriveUpdate(RetrieveUpdateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# Retrieve details or delete a specific vendor


class VendorRetriveDelete(RetrieveDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# purchase order

# List all purchase orders or create a new purchase order


class PurchaseOrderListCreate(ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        if not queryset.exists():

            return Response({"message": "No purchase order found"}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data, status=status.HTTP_200_OK)

# Retrieve details or update a specific purchase order


class PurchaseOrderRetriveUpdate(RetrieveUpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# Retrieve details or delete a specific purchase order


class PurchaseOrderRetriveDelete(RetrieveDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# Acknowledge the receipt of a purchase order.


class AcknowledgeUpdate(UpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = AcknowledgeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.validated_data['acknowledgment_date'] = timezone.now()
        super().perform_update(serializer)
        return Response(serializer.data)

# Retrieve performance details of a specific vendor


class VendorPerformance(RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = PerformanceSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
