from django.db import models

# Create your models here.

class VandeeDetails(models.Model):

    user_type = models.TextChoices('VANDEE', 'VENDOR')
    vandee_id = models.AutoField(primary_key=True)
    vandee_realName = models.CharField(max_length=40)
    vandee_email = models.EmailField(max_length=30)
    vandee_phone = models.IntegerField(max_length=15)



    def __str__(self):
        return self.name

class VandeeCdo(models.Model):

    item_no = models.IntegerField(max_length=500)
    item_name = models.CharField(max_length=40)
    quantity = models.IntegerField(max_length=800)

    def __str__(self):
        return self.name

class VandeeVdo(models.Model):

    delivery_orderId = models.AutoField(primary_key=True)
    item_no = models.IntegerField(max_length=500)
    item_name = models.CharField(max_length=40)
    quantity = models.IntegerField(max_length=800)

    def __str__(self):
        return self.name

class VandeeVerifyInvoice(models.Model):

    Invoice_id = models.AutoField(primary_key=True)
    item_types = models.IntegerField(max_length=500)
    vandee_id = models.IntegerField(max_length=800)
    verfication_status = models.CharField(max_length=40)


    def __str__(self):
        return self.name

