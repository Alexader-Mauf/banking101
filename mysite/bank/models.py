from django.db import models


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(
        max_length=255
    )
    name = models.CharField(
        max_length=255
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Account(models.Model):
    user_id = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='accounts'
    )
    balance = models.DecimalField(max_digits=22,decimal_places=4)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class transfers(models.Model):
    acc_from = models.ForeignKey(
        Customer,
        on_delete= models.CASCADE,
        related_name='user_that_send'
    )
    acc_to = models.ForeignKey(
        Customer,
        on_delete= models.CASCADE,
        related_name='user_that_recieved'
    )
    total = models.DecimalField(max_digits=22,decimal_places=4)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)