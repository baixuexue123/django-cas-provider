# -*- coding: utf-8 -*-
import urllib

from django.utils.crypto import get_random_string

from .models import ServiceTicket, LoginTicket


def add_qs(url, **kwargs):
    qs = urllib.urlencode(kwargs)
    if not qs:
        return url
    if '?' in url:
        return url+'?'+qs
    else:
        return url+'&'+qs


def create_service_ticket(user, service):
    """
    Creates a new service ticket for the specified user and service.
    """
    ticket_string = 'ST-' + get_random_string(length=29)  # Total ticket length = 29 + 3 = 32
    ticket = ServiceTicket(service=service, user=user, ticket=ticket_string)
    ticket.save()
    return ticket


def create_login_ticket():
    """
    Creates a new login ticket for the login form. Uses _generate_string.
    """
    ticket_string = 'LT-' + get_random_string(length=29)
    ticket = LoginTicket(ticket=ticket_string)
    ticket.save()
    return ticket_string
