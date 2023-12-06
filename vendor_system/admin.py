from django.contrib import admin

from vendor_system.models import HistoricalPerformance, PurchaseOrder, Vendor

# Register your models here.


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'contact_details', 'address', 'vendor_code', 'on_time_delivery_rate',
                    'quality_rating_avg', 'average_response_time', 'fulfillment_rate']
    list_per_page = 10
    search_fields = ['name', 'vendor_code']


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'po_number', 'vendor', 'order_date',
                    'delivery_date', 'items', 'quantity', 'status', 'quality_rating', 'issue_date', 'acknowledgment_date']
    list_per_page = 10
    list_editable = ['quality_rating', 'status']
    list_filter = ['status']
    search_fields = ['po_number']


@admin.register(HistoricalPerformance)
class HistoricalPerformanceAdmin(admin.ModelAdmin):
    list_display = ['vendor', 'date', 'on_time_delivery_rate',
                    'quality_rating_avg', 'average_response_time', 'fulfillment_rate']
    list_per_page = 10
