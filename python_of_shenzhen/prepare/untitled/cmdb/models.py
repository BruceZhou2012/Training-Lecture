from django.db import models


class ServerBaseInfo(models.Model):
    uuid = models.CharField(max_length=50, unique=True, null=True, blank=True)
    sn = models.CharField(max_length=50, unique=True, null=True, blank=True)
    idc = models.CharField(max_length=20, null=True, blank=True)
    rack_location = models.CharField(max_length=20, null=True, blank=True)
    private_ip = models.CharField(max_length=20, null=True, blank=True)
    ram = models.CharField(max_length=10, null=True, blank=True)
    buy_date = models.CharField(max_length=20, null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    cpu_count = models.CharField(max_length=3, null=True, blank=True)
    kernel_version = models.CharField(max_length=40, null=True, blank=True)
    env = models.CharField(max_length=20, null=True, blank=True)
    dev_type = models.CharField(max_length=20, null=True, blank=True)


class UpdateInfo(ServerBaseInfo):
    catalog = models.CharField(max_length=50, null=True, blank=True)
    appname = models.CharField(max_length=64, null=True, blank=True)
    status = models.CharField(max_length=6, null=True, blank=True)
    op_duty = models.CharField(max_length=20, null=True, blank=True)
    rd_duty = models.CharField(max_length=20, null=True, blank=True)
    hostname = models.CharField(max_length=64, null=True, blank=True)
    catalog_branch = models.CharField(max_length=50, null=True, blank=True)