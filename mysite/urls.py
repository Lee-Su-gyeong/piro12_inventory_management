from django.contrib import admin
from django.urls import path, include
from product.views import product_list, product_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls')),
    path('', include('people.urls')),

]
