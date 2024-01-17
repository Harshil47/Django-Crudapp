from django.urls import path
from . import views

urlpatterns = [
    path('ofv/', views.orderFormView, name='order_url'),
    path('sv/', views.showView, name='show_url'),
    path('up/<int:f_oid>', views.updateView, name= 'update_url'),
    path('del/<int:f_oid>', views.deleteView, name= 'delete_url'),
    path('export-csv/', views.export_csv, name='export_csv_url'),
    path('customer-info/', views.customer_info, name='customer_info_url'),
    path('customer-add/', views.customer_add, name='customer_add_url'),
    path('get-product-details/<str:product_id>/', views.get_product_details, name='get_product_details'),
    path('bill/', views.billView, name='bill_url'),
    path('rate/<int:oid>/', views.rateView, name='rate_url'),
    path('submit/<int:oid>', views.rateView, name='submit_url'),
    path('show-bill/', views.showBillView, name='showBill_url'),
    path('print-docx/', views.printDocxView, name='print_docx_url'),
    
]