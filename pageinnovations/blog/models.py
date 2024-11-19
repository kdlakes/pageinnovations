from django.db import models
import re
# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='assets/images/', blank=True, null=True)

    def _str_(self):
        return self.title
    
    def word_count(self):
        # Remove special characters and split by whitespace
        words = re.findall(r'\w+', self.content)
        return len(words)
    

class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    # created_date = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='assets/images/', blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
    def _str_(self):
        return self.name