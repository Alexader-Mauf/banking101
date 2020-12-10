from django.db import models, transaction


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

    @transaction.atomic()
    def make_transaction(self, accfrom, accto, amount):
        new_transfer = Transfer(acc_from=accfrom, acc_to=accto, total=amount)
        debitor = Account.objects.get(pk=accfrom)
        creditor = Account.objects.get(pk=accto)
        debitor.balance += -amount
        creditor.balance += amount
        return "Transaction Complete"


    def __str__(self):
        return "{} {} {}".format(self.id,self.first_name,self.name)




class Account(models.Model):
    user_id = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='accounts',
        null=True
    )
    balance = models.DecimalField(max_digits=22,decimal_places=4)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def add_money(self, value):
        self.balance += value


    def pay_money(self, value):
        self.balance += -value


    def __str__(self):
        return (self.pk)



class Transfer(models.Model):
    acc_from = models.ForeignKey(
        Customer,
        on_delete= models.CASCADE,
        related_name='user_that_send',
        null=True
    )
    acc_to = models.ForeignKey(
        Customer,
        on_delete= models.CASCADE,
        related_name='user_that_recieved',
        null=True
    )
    total = models.DecimalField(max_digits=22,decimal_places=4)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Transaktion {} zwischen {} und {}".format(self.pk,self.acc_to,self.acc_from)