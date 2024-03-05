from django.db import models

# Create your models here.
class productcategory(models.Model):
    productcategory_name=models.CharField(max_length=100)
    productcategory_id=models.IntegerField(primary_key=True)

    def __str__(self):
        return self.productcategory_name

class products(models.Model):
    productcategory_id=models.ForeignKey(productcategory,on_delete=models.CASCADE)
    productprice=models.IntegerField()
    productname=models.CharField(max_length=100)
    productid=models.IntegerField()



