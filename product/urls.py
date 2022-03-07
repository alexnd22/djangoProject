from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from product import views

urlpatterns = [
    path('create-product/', views.ProductCreateView.as_view(), name='create_product'),
    path('list-of-products/', views.ProductListView.as_view(), name='list_of_products'),
    path('update-product/<int:pk>/', views.ProductUpdateView.as_view(), name='update_product'),
    path('delete-product/<int:pk>/', views.ProductDeleteView.as_view(), name='delete_product'),
    path('delete-product-popup/<int:pk>/', views.delete_product_with_popup, name='delete_with_popup'),
    path('detail-product/<int:pk>/', views.ProductDetailView.as_view(), name='detail_product'),
    path('detail-product-with-popup/<int:pk>/', views.delete_product_with_popup, name='detail_product_with_popup'),
    path('products-per-category/<int:pk>/', views.get_products_per_category, name='products_per_category')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

