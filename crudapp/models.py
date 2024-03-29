from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    quantity_per = models.FloatField()
    pcs_fts = models.FloatField()
    rate = models.FloatField()
    tax_rate = models.FloatField()
    hsn_code = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Orders(models.Model):
    oid = models.AutoField(primary_key=True) 
    fname = models.CharField(max_length=20)
    Cname = models.CharField(max_length=20)
    Pname = models.CharField(max_length=100)
    Dname = models.CharField(max_length=20)
    Lno = models.CharField(max_length=20)
    pcno = models.CharField(max_length=20)
    scno = models.CharField(max_length=20)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    trip = models.FloatField()
    df1 = models.DateField(null=True, blank=True)
    df2 = models.DateField(null=True, blank=True)
    df3 = models.DateField(null=True, blank=True)
    pcs = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    width = models.FloatField(null=True, blank=True)
    length = models.FloatField(null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)
    billed = models.CharField(max_length=3, default='No')
    AggregatedAmount = models.FloatField(null=True, blank=True)
    AggregatedQuantity = models.FloatField(null=True, blank=True)
    mergedOids = models.CharField(max_length=255, blank=True, null=True)
    

    def __str__(self):
        return f'{self.fname},{self.product}'
    
class Customer(models.Model):
    Cname = models.CharField(max_length=20, primary_key=True)
    group = models.CharField(max_length=20)
    adr = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    gst = models.CharField(max_length=20)
    pan = models.CharField(max_length=20)
    state = models.CharField(max_length=30, null=True, blank=True)
    code = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.Cname}'
    

class Billing(models.Model):
    MCODE_CHOICES = [
        ('M1', 'M1'),
        ('M2', 'M2'),
        # Add more choices as needed
    ]

    TCODE_CHOICES = [
        ('T1', 'T1'),
        ('T2', 'T2'),
        # Add more choices as needed
    ]
    bill_id = models.AutoField(primary_key=True)
    Cname = models.CharField(max_length=20)
    bill_date = models.DateField(null=True, blank=True)
    final_rate = models.FloatField(null=True, blank=True)
    material_rate = models.FloatField(null=True, blank=True)
    transport_rate = models.FloatField(null=True, blank=True)
    final_amount = models.FloatField(null=True, blank=True)
    mcode = models.CharField(max_length=20, choices=MCODE_CHOICES)
    tcode = models.CharField(max_length=20, choices=TCODE_CHOICES)
    
    oid = models.IntegerField()  # Assuming oid is an integer, update the field type as needed
    product = models.CharField(max_length=50)  # Update the max_length as needed
    place = models.CharField(max_length=50)  # Update the max_length

    def __str__(self):
        return f'Bill ID: {self.bill_id}'

class Record(models.Model):
    record_id = models.AutoField(primary_key=True) 
    Invoice = models.CharField(max_length=50,null=True, blank=True)
    Cname = models.CharField(max_length=20)
    Cadr = models.CharField(max_length=100)
    Sadr = models.CharField(max_length=100)
    state = models.CharField(max_length=30, null=True, blank=True)
    code = models.FloatField(null=True, blank=True)
    gst = models.CharField(max_length=20, null=True, blank=True)
    date = models.DateField()
    InvoiceEnd = models.DateField(null=True, blank=True)
    tax_rate = models.FloatField(null=True, blank=True)
    lorry_no = models.CharField(max_length=20)
    trip = models.FloatField()
    challan = models.CharField(max_length=20)
    hsn = models.CharField(max_length=20)
    product = models.CharField(max_length=20)
    aggregated_quantity = models.FloatField()
    rate = models.FloatField()
    aggregated_amount = models.FloatField()
    cgst = models.FloatField()
    sgst = models.FloatField()
    final_amount = models.FloatField()
    total_amount = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'Record ID: {self.record_id}'


class TempTable(models.Model):
    end_date = models.DateField(null=True, blank=True)