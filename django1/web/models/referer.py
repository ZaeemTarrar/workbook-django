import datetime
import json

from django import forms
from django.core import serializers
from django.db import models

# Create your models here.
from django.utils import timezone


# from utils.json_helper import json_stringify


class Referer(models.Model):
    """
    Fields of the Table Model Class
    """
    firstname = models.CharField("firstname", blank=False, max_length=30)
    middlename = models.CharField("middleware", blank=False, max_length=30)
    lastname = models.CharField("lastname", blank=False, max_length=30)
    cnic = models.CharField("cnic", blank=False, max_length=30)
    designation = models.CharField("designation", blank=False, max_length=30)
    address = models.CharField("address", blank=False, max_length=30)
    snap = models.TextField("snap")

    created_at = models.DateTimeField('date.created', default=timezone.now)
    updated_at = models.DateTimeField('date.updated', default=timezone.now)

    """
    Table Model Meta Data
    """

    class Meta:
        db_table = u'referer'

    def was_published_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)

    """
    Model Data Formations
    """

    @staticmethod
    def base_format():
        return {
            "firstname": None,
            "middlename": None,
            "lastname": None,
            "cnic": None,
            "address": None,
            "designation": None,
            "snap": None,
        }

    @staticmethod
    def format(self, firstname=None, middlename=None, lastname=None, cnic=None, address=None, designation=None,
               snap=None):
        creation_date = self.created_at.strftime("%m/%d/%Y")
        creation_time = self.created_at.strftime('%H:%M:%S %p')
        updated_date = self.updated_at.strftime("%m/%d/%Y")
        updated_time = self.updated_at.strftime('%H:%M:%S %p')
        return {
            "firstname": firstname,
            "middlename": middlename,
            "lastname": lastname,
            "cnic": cnic,
            "address": address,
            "designation": designation,
            "snap": snap,
            "created_at": {
                "date": creation_date,
                "time": creation_time
            },
            "updated_at": {
                "date": updated_date,
                "time": updated_time
            }
        }

    def getSelfData(self):
        return Referer.format(self, self.firstname, self.middlename, self.lastname, self.cnic, self.address,
                              self.designation, self.snap)

    """
    Override Hooks
    """

    def save(self, *args, **kwargs):
        super().save(self, *args, **kwargs)
        return self.getSelfData()

    """
    Table Model Custom Static Methods
    """

    @staticmethod
    def fetch_all():
        # return json_stringify(Product.objects.all())
        pass
