from django.urls import path

from vendor_system import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.home_page, name='home'),
    path('api/vendors/', views.VendorListCreate.as_view()),
    path('api/vendors/<int:pk>/', views.VendorRetriveUpdate.as_view()),
    path('api/vendors/delete/<int:pk>/', views.VendorRetriveDelete.as_view()),
    path('api/purchase-orders/', views.PurchaseOrderListCreate.as_view()),
    path('api/purchase-orders/<int:pk>/',
         views.PurchaseOrderRetriveUpdate.as_view()),
    path('api/purchase-orders/delete/<int:pk>/',
         views.PurchaseOrderRetriveDelete.as_view()),
    path('api/purchase-orders/<int:pk>/acknowledge/',
         views.AcknowledgeUpdate.as_view()),
    path('api/vendors/<int:pk>/performance/',
         views.VendorPerformance.as_view()),
    path('apitoken/', obtain_auth_token),
]
