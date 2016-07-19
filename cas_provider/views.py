# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.conf import settings

from .utils import add_qs, create_service_ticket
from .forms import LoginForm
from .models import ServiceTicket, LoginTicket


def login(request, template_name='cas/login.html', success_redirect=None):
    if success_redirect is None:
        success_redirect = settings.LOGIN_REDIRECT_URL or '/accounts/profile/'

    service = request.GET.get('service', None)
    if request.user.is_authenticated():
        if service is not None:
            ticket = create_service_ticket(request.user, service)
            return HttpResponseRedirect(add_qs(service, ticket=ticket.ticket))
        else:
            return HttpResponseRedirect(success_redirect)

    errors = []
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        service = request.POST.get('service', None)
        lt = request.POST.get('lt', None)

        try:
            login_ticket = LoginTicket.objects.get(ticket=lt)
        except LoginTicket.DoesNotExist:
            errors.append('Login ticket expired. Please try again.')
        else:
            login_ticket.delete()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    if service is not None:
                        ticket = create_service_ticket(user, service)
                        return HttpResponseRedirect(add_qs(service, ticket=ticket.ticket))
                    else:
                        return HttpResponseRedirect(success_redirect)
                else:
                    errors.append('This account is disabled.')
            else:
                errors.append('Incorrect username and/or password.')
    form = LoginForm(service)
    return render_to_response(template_name, {'form': form, 'errors': errors},
                              context_instance=RequestContext(request))


def validate(request):
    service = request.GET.get('service', None)
    ticket_string = request.GET.get('ticket', None)
    if service is not None and ticket_string is not None:
        try:
            ticket = ServiceTicket.objects.get(ticket=ticket_string)
        except ServiceTicket.DoesNotExist:
            pass
        else:
            username = ticket.user.username
            ticket.delete()
            return HttpResponse("yes\n%s\n" % username)
    return HttpResponse("no\n\n")


def logout(request, template_name='cas/logout.html'):
    url = request.GET.get('url', None)
    auth_logout(request)
    return render_to_response(template_name, {'url': url}, context_instance=RequestContext(request))
