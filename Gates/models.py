from django.db import models
# Create your models here.
class Fuelgate(models.Model):
    fuelid = models.AutoField(primary_key=True)
    vehicleno = models.TextField(blank=True, null=True)
    slipno = models.TextField(blank=True, null=True)
    challanno = models.TextField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    fueltime = models.DateTimeField(blank=True, null=True)
    vehicleid = models.IntegerField(blank=True, null=True)
    fuelslipno = models.TextField(blank=True, null=True)
    username = models.TextField(blank=True, null=True)
    slipid = models.IntegerField(blank=True, null=True)
    transporter = models.TextField(blank=True, null=True)
    transporterid = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    locationid = models.IntegerField(blank=True, null=True)
    wheeler = models.IntegerField(blank=True, null=True)
    driver = models.TextField(blank=True, null=True)
    driverid = models.IntegerField(blank=True, null=True)
    fuelbyrule = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fuelgate'

class Ingate(models.Model):
    slipid = models.AutoField(primary_key=True)
    sliptime = models.DateTimeField(blank=True, null=True)
    vehicleno = models.TextField(blank=True, null=True)
    destination = models.TextField(blank=True, null=True)
    loading = models.TextField(blank=True, null=True)
    dlno = models.TextField(blank=True, null=True)
    transporter = models.TextField(blank=True, null=True)
    gate = models.TextField(blank=True, null=True)
    currentlogin = models.TextField(blank=True, null=True)
    driver = models.TextField(blank=True, null=True)
    controlno = models.BigIntegerField(blank=True, null=True)
    driverid = models.BigIntegerField(blank=True, null=True)
    tare = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    rfid = models.BigIntegerField(blank=True, null=True)
    rfno = models.TextField(blank=True, null=True)
    locationid = models.IntegerField(blank=True, null=True)
    transporterid = models.IntegerField(blank=True, null=True)
    vehicleid = models.IntegerField(blank=True, null=True)
    validslip = models.BooleanField(blank=True, null=True)
    slipno = models.TextField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    fueltime = models.DateTimeField(blank=True, null=True)
    fueloperator = models.TextField(blank=True, null=True)
    wheeler = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingate'

class Outgate(models.Model):
    challanid = models.AutoField(primary_key=True)
    slipno = models.TextField(blank=True, null=True)
    slipid = models.BigIntegerField(blank=True, null=True)
    vehicleno = models.TextField(blank=True, null=True)
    driver = models.TextField(blank=True, null=True)
    driverid = models.BigIntegerField(blank=True, null=True)
    loading = models.TextField(blank=True, null=True)
    destination = models.TextField(blank=True, null=True)
    challanno = models.TextField(blank=True, null=True)
    gross = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    tare = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    net = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    passdate = models.DateTimeField(blank=True, null=True)
    passgate = models.TextField(blank=True, null=True)
    sliptime = models.DateTimeField(blank=True, null=True)
    challantime = models.DateTimeField(blank=True, null=True)
    printtime = models.DateTimeField(blank=True, null=True)
    material = models.TextField(blank=True, null=True)
    weighbridge = models.TextField(blank=True, null=True)
    vehicleid = models.IntegerField(blank=True, null=True)
    locationid = models.IntegerField(blank=True, null=True)
    username = models.TextField(blank=True, null=True)
    transporterid = models.IntegerField(blank=True, null=True)
    transporter = models.TextField(blank=True, null=True)
    challannet = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    grosswbid = models.IntegerField(blank=True, null=True)
    grosswb = models.TextField(blank=True, null=True)
    tarewbid = models.IntegerField(blank=True, null=True)
    tarewb = models.TextField(blank=True, null=True)
    passoperator = models.TextField(blank=True, null=True)
    wbdatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'outgate'

class Railwaysiding(models.Model):
    entryid = models.AutoField(primary_key=True)
    vehicleno = models.TextField(blank=True, null=True)
    grosswb = models.TextField(blank=True, null=True)
    gross = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    tarewb = models.TextField(blank=True, null=True)
    tare = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    net = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    entrytime = models.DateTimeField(blank=True, null=True)
    shortage = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    exittime = models.DateTimeField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    vehicleid = models.IntegerField(blank=True, null=True)
    challannet = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    challanno = models.TextField(blank=True, null=True)
    slipno = models.TextField(blank=True, null=True)
    grosswbid = models.IntegerField(blank=True, null=True)
    tarewbid = models.IntegerField(blank=True, null=True)
    usergross = models.TextField(blank=True, null=True)
    usertare = models.TextField(blank=True, null=True)
    wbdatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'railwaysiding'
