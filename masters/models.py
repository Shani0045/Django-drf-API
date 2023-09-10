# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
class Drivers(models.Model):
    driverid = models.BigIntegerField(primary_key=True)
    drivername = models.TextField(blank=True, null=True)
    dlno = models.TextField(unique=True, blank=True, null=True)
    dltype = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    dlexpiry = models.DateField(blank=True, null=True)
    isactive = models.BooleanField(blank=True, null=True)
    drivermobile = models.TextField(blank=True, null=True)
    fingerprint = models.TextField(blank=True, null=True)
    faceprint = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    statuschangedate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drivers'

class Locations(models.Model):
    locationid = models.IntegerField(primary_key=True)
    location = models.TextField(blank=True, null=True)
    locationcode = models.TextField(blank=True, null=True)
    createdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locations'

class Owners(models.Model):
    ownerid = models.AutoField(primary_key=True)
    ownername = models.TextField(blank=True, null=True)
    address1 = models.TextField(blank=True, null=True)
    address2 = models.TextField(blank=True, null=True)
    pan = models.TextField(blank=True, null=True)
    aadhar = models.TextField(blank=True, null=True)
    mobile = models.TextField(blank=True, null=True)
    gst = models.TextField(blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    dlno = models.TextField(blank=True, null=True)
    isactive = models.BooleanField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    statuschangedate = models.DateField(blank=True, null=True)
    stateid = models.IntegerField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    pincode = models.TextField(blank=True, null=True)
    bankname = models.TextField(blank=True, null=True)
    accountno = models.TextField(blank=True, null=True)
    ifsc = models.TextField(blank=True, null=True)
    transportercode = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'owners'

class Vehicles(models.Model):
    vehicleid = models.AutoField(primary_key=True)
    vehicleno = models.TextField(blank=True, null=True)
    compliant = models.IntegerField(blank=True, null=True)
    ownerid = models.BigIntegerField(blank=True, null=True)
    ownername = models.TextField(blank=True, null=True)
    ownermobile = models.TextField(blank=True, null=True)
    rcno = models.TextField(blank=True, null=True)
    tempno = models.TextField(blank=True, null=True)
    chasisno = models.TextField(blank=True, null=True)
    fitnessexpiry = models.DateField(blank=True, null=True)
    insuranceexpiry = models.DateField(blank=True, null=True)
    permitexpiry = models.DateField(blank=True, null=True)
    pollutionexpiry = models.DateField(blank=True, null=True)
    permittype = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    statuschangedate = models.DateField(blank=True, null=True)
    createdate = models.DateField(blank=True, null=True)
    ownerpan = models.TextField(blank=True, null=True)
    rfno = models.TextField(blank=True, null=True)
    rfid = models.BigIntegerField(blank=True, null=True)
    permit = models.TextField(blank=True, null=True)
    insurance = models.TextField(blank=True, null=True)
    pollution = models.TextField(blank=True, null=True)
    fitness = models.TextField(blank=True, null=True)
    isactive = models.BooleanField(blank=True, null=True)
    roadtax = models.TextField(blank=True, null=True)
    roadtaxexpiry = models.DateTimeField(blank=True, null=True)
    rcdate = models.DateTimeField(blank=True, null=True)
    wheeler = models.IntegerField(blank=True, null=True)
    vowner = models.TextField(blank=True, null=True)
    vcontact = models.TextField(blank=True, null=True)
    vaddress = models.TextField(blank=True, null=True)
    vownership = models.BooleanField(blank=True, null=True)
    gpsdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicles'

class Weighbridge(models.Model):
    wbid = models.AutoField(primary_key=True)
    wbname = models.TextField(blank=True, null=True)
    locationid = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    capacity = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weighbridge'
