from rateExchanger.models import Exchange
from django.core.exceptions import ObjectDoesNotExist

def rateExists(from_currency, to_currency, date):
    try:
        ex = Exchange.objects.get(from_currency=from_currency, to_currency=to_currency, date=date)
        return ex.rate
    except ObjectDoesNotExist:
        return None