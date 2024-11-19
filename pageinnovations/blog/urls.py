from django.urls import path
from .import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('post-detail/<int:id>', views.post_detail, name='post_detail'),
    path('product-detail/<int:id>', views.product_detail, name='product_detail'),

  
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root =  settings.MEDIA_ROOT)