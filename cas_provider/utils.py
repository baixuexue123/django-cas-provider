# -*- coding: utf-8 -*-
from urllib import urlencode
from urlparse import parse_qsl, urlparse, urlunparse

from django.conf import settings
from django.utils.crypto import get_random_string
from django.utils.encoding import force_bytes

from .models import ServiceTicket, LoginTicket


def add_query_params(url, params):
    """
    Inject additional query parameters into an existing URL. If
    parameters already exist with the same name, they will be
    overwritten. Parameters with empty values are ignored. Return
    the modified URL as a string.
    """
    def encode(s):
        return force_bytes(s, settings.DEFAULT_CHARSET)
    params = dict([(encode(k), encode(v)) for k, v in params.items() if v])

    parts = list(urlparse(url))
    query = dict(parse_qsl(parts[4]))
    query.update(params)
    parts[4] = urlencode(query)
    return urlunparse(parts)


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
