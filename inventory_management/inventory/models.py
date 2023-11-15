from django.db import models

class Inventory(models.Model):
    id = models.AutoField(primary_key = True)
    created_at = models.DateTimeField(auto_now=True)
    item_name = models.TextField(default="")
    item_count = models.TextField(default="")
    supplier_id = models.IntegerField(default=0)
    ordered_date = models.DateField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.item_name


class SupplierList(models.Model):
    id = models.AutoField(primary_key = True)
    created_at = models.DateTimeField(auto_now=True)
    name = models.TextField(default="")
    address = models.TextField(default="")
    contact_no = models.TextField(default="")

    def __str__(self):
        return self.name
