from django.shortcuts import render, redirect
import random, string
from .models import Url
from django.contrib import messages
from serivces.vaidator import UrlRegexValidator
from django.core.exceptions import ValidationError


# regex = re.compile(
#     r'^(?:http|ftp)s?://'  # http:// or https://
#     r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
#     r'localhost|'  # localhost...
#     r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
#     r'(?::\d+)?'
#     r'(?:/?|[/?]\S+)$', re.IGNORECASE)


def getAlias():
    return ''.join([random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(8)])


def dashboard(request):
    if request.method == 'POST':
        URL = request.POST['URL']
        alias = request.POST.get('alias', None)
        if not alias:
            alias = getAlias()
        try:
            UrlRegexValidator().validate_url(URL)
            Url.objects.create(user=request.user, target_url=URL, alias=alias).save()
            messages.success(request, 'shorted success')
            return redirect('dashboard')
        except ValidationError:
            messages.error(request, 'Make short url error')
            return render(request, 'dashboard.html', {'url': URL, 'alias': alias})
        except:
            messages.error(request, 'Alias already used')
            return render(request, 'dashboard.html', {'url': URL, 'alias': alias})
    site = request.get_host()
    return render(request, 'dashboard.html', {'domain': site})


def redirect_to_target_page(request, alias):
    obj = Url.objects.get(alias=alias)
    URL = obj.target_url
    return redirect(URL)
