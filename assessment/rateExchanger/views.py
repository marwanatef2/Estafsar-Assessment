from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime, date
import requests
from .models import Exchange
from .utils import rateExists

FRANKFURTER_HOST = "https://api.frankfurter.app"

def rate(request):
    on_date = request.GET.get('date', date.today())
    if isinstance(on_date, str):
        on_date = datetime.strptime(on_date, "%Y-%m-%d").date()
    from_currency = request.GET.get('from', 'EUR')
    to_currency = request.GET.get('to')

    # check if rate is already in DB
    existing_rate = rateExists(from_currency, to_currency, on_date)

    if existing_rate is not None:
        return JsonResponse({'rate': existing_rate})
    else:
        # get new rate from external api

        # set query params
        if to_currency is not None:
            payload = {
                "from": from_currency,
                "to": to_currency
            }
        else:
            payload = {
                "from": from_currency
            }

        res = requests.get('{}/{}'.format(FRANKFURTER_HOST, on_date), params=payload)

        if res.status_code == 200:
            if not to_currency:
                rates = res.json()['rates']
                return JsonResponse({'base': from_currency, 'rates': rates})
            else:
                ex_rate = res.json()['rates'][to_currency]
                exchange = Exchange(from_currency=from_currency, to_currency=to_currency, date=on_date, rate=ex_rate)
                exchange.save()
                return JsonResponse({'rate': ex_rate})

        else:
            return JsonResponse({'message': "Not found"}, status=404)
