from django.db import models  
class Customer(models.Model):  
    customer_id = models.CharField(max_length=20)  
    customer_name = models.CharField(max_length=100)  
    customer_address =models.CharField(max_length=200)
    service_id = models.CharField(max_length=20)  
    class Meta:  
        db_table = "customer"  