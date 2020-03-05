from django.db import models

# Create your models here.
class Category(models.Model):
    idC = models.BigAutoField(primary_key=True)
    parentCategory = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    name = models.CharField('Category', max_length = 100)
    image = models.ImageField(upload_to='photos_category',null=True)

    def __str__(self):
        return self.name
    
    


class Product(models.Model):   
    idP = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    weight = models.FloatField()
    prize = models.FloatField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos_products',null=True)

    def __str__(self):
        return self.name
