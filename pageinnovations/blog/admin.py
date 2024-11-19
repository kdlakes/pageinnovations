from django.contrib import admin
from .models import ContactMessage  
from .models import BlogPost
from .models import Product

# Register your models here.

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content','created_date', 'image')
    list_filter = ('title', 'created_date')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email')
    search_fields = ('first_name', 'email', 'message')
    list_filter =  ('email',)
    list_per_page = 20



@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'category', 'created_at', 'image')
    list_filter = ('name', 'price', 'created_at')
    list_per_page = 40