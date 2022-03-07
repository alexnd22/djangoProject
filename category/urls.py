from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from category import views, insert

urlpatterns = [
    path('create-category/', views.CategoryCreateView.as_view(), name='create_category'),
    path('list-of-categories/', views.CategoryListView.as_view(), name='list_of_categories'),
    path('update-category/<int:pk>/', views.CategoryUpdateView.as_view(), name='update_category'),
    path('delete-category/<int:pk>/', views.CategoryDeleteView.as_view(), name='delete_category'),
    path('delete-category-popup/<int:pk>/', views.delete_category_with_popup, name='delete_with_popup'),
    path('detail-category/<int:pk>/', views.CategoryDetailView.as_view(), name='detail_category'),
    path('detail-category-with-popup/<int:pk>/', views.delete_category_with_popup, name='detail_category_with_popup'),
    path('import-data/', insert.import_data, name='import_data')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
