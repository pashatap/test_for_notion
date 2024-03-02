from django.urls import path

from .views import AllProductsView, ProductDetailView, ProductView, CreateOrderView

app_name = 'system'
urlpatterns = [
    path('', ProductView.as_view(), name="products"),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('all_product', AllProductsView.as_view(), name='all_product'),
    path('all_product/<int:pk>', CreateOrderView.as_view(), name='create_order')

]
