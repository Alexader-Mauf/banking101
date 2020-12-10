from django.db import models


#create your models here

class Customer(models.Model):
    created_at = models.DateTimeField('created_at')
    updated_at = models.DateTimeField('updated_at')
    name = models.CharField('Name')
    first_name = models.CharField('Vorname')


class Account(models.Model):
    created_at = models.DateTimeField('created_at')
    updated_at = models.DateTimeField('updated_at')
    user_id = models.ForeignKey(Customer,on_delete=models.CASCADE())
    balance = models.DecimalField(22,4,'Kontostand')



class transfer(models.Model):
    created_at = models.DateTimeField('created_at')
    updated_at = models.DateTimeField('updated_at')
    total = models.DecimalField(22,4,"Überwiesener Betrag")
    from_acc = models.ForeignKey("from_acc_id")
    to_acc = models.ForeignKey("to_acc_id")