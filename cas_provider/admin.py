# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import ServiceTicket, LoginTicket


@admin.register(ServiceTicket)
class ServiceTicketAdmin(admin.ModelAdmin):
    pass


@admin.register(LoginTicket)
class LoginTicketAdmin(admin.ModelAdmin):
    pass
