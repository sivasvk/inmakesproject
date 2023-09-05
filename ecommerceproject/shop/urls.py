from . import views
from django.urls import path

app_name = 'shop'
urlpatterns = [
    path('', views.allProdCat, name='allProdCat'),
    path('', views.allProdCate, name='allProdCate'),
    path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatDetail')
]
