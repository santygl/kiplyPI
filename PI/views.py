from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_protect
from django import forms


@csrf_protect
def register2(request, template_name='registration/register2.html',
              redirect_field_name=REDIRECT_FIELD_NAME,
              authentication_form=AuthenticationForm,
              extra_context=None):
    redirect_to = request.POST.get(redirect_field_name,
                                   request.GET.get(redirect_field_name, ''))
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        context = None
        if form.is_valid():
            user = form.save()
            return TemplateResponse(request, template_name, context)
        else:
            current_site = get_current_site(request)
            context = {
                'form': form,
                redirect_field_name: redirect_to,
                'site': current_site,
                'site_name': current_site.name,
            }
            if extra_context is not None:
                context.update(extra_context)

            return TemplateResponse(request, template_name, context)

    else:
        form = UserCreationForm()  # An unbound form
        current_site = get_current_site(request)
        context = {
            'form': form,
            redirect_field_name: redirect_to,
            'site': current_site,
            'site_name': current_site.name,
        }
        if extra_context is not None:
            context.update(extra_context)

        return TemplateResponse(request, template_name, context)
