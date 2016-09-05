# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class ServiceTicket(models.Model):
    user = models.ForeignKey(User)
    service = models.URLField(verify_exists=False)
    ticket = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s (%s) - %s" % (self.user.username, self.service, self.created_on)


class LoginTicket(models.Model):
    ticket = models.CharField(max_length=32)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s - %s" % (self.ticket, self.created_on)
