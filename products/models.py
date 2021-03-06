from django.db import models


# In order to connect with database ```python3 manage.py makemigrations```
# then `python3 manage.py migrate`
class Products(models.Model):          # Class name will be displayed on website
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    Buy_link = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=15)
    description = models.CharField(max_length=1500)
    discount = models.FloatField()