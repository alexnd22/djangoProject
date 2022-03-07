from django.urls import path

from home import views

urlpatterns = [
    path('index/', views.index, name='index1'),
    path('all-students/', views.students, name='all_stundents'),
    path('all-brands/', views.brands, name='all_brands'),
    path('', views.HomeTemplateView.as_view(), name='homepage')
]
