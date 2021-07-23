from django.conf import SettingsReference, settings
from CoinApp.settings import COIN_API_KEY, EMAIL_HOST_USER
from django.core.mail import send_mail
from celery.utils.log import get_task_logger
from celery import shared_task
from datetime import datetime

import json
import requests

from app.models import ValueAlert, PercentageAlert, User, Alert

logger = get_task_logger(__name__)


@shared_task
def sendAlert():
    base_url = "https://rest.coinapi.io/v1/exchangerate/{}/{}"
    headers = {"X-CoinAPI-Key": COIN_API_KEY}

    for alert in ValueAlert.objects.filter(activated=True):

        crypto = alert.crypto
        currency = alert.currency
        value = alert.value
        direction = alert.direction

        url = base_url.format(crypto, currency)
        response = requests.get(url, headers=headers)
        json_response = json.loads(response.text)

        api_value = json_response["rate"]

        user = alert.user
        email = user.email

        subject = "🔔 CoinApp Alert 🔔"
        if (direction == 'A') and (api_value >= value):
            message = f" Hello {user} !\n {crypto} is above {value} {currency} !"

        elif (direction == "B") and (api_value <= value):
            message = f" Hello {user} !\n {crypto} is below {value} {currency} !"
        
        else:
            break

        from_email = EMAIL_HOST_USER
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list)

        alert.activated = False
        alert.save()

    for alert in PercentageAlert.objects.filter(activated=True):

        time_url = "https://rest.coinapi.io/v1/exchangerate/{}/{}?time={}"

        crypto = alert.crypto
        currency = alert.currency
        timeframe = alert.timeframe
        percentage = alert.percentage
        direction = alert.direction

        url1 = base_url.format(crypto, currency)
        response = requests.get(url, headers=headers)
        json_response = json.loads(response.text)

        date2 = datetime.now() - timeframe
        url2 = time_url.format(crypto, currency, date2.replace(microseconds=0).isoformat())
        response2 = requests.get(url2, headers=headers)
        json_response2 = json.loads(response2.text)

        api_value1 = json_response["rate"]
        api_value2 = json_response2["rate"]

        up_percent = 1 + (percentage / 100)
        down_percent = 1 - (percentage / 100)

        if ((direction == 'U' and (up_percent * api_value2) >= api_value1) or direction == 'D' and (down_percent * api_value2) <= api_value1):

            user = alert.user
            email = user.email

            subject = "🔔 CoinApp Alert 🔔"
            if (direction == 'U'):
                message = f" Hello {user} !\n {crypto} has increased of {percentage} % !"

            elif (direction == 'D'):
                message = f" Hello {user} !\n {crypto} has decreased of {percentage} % !"

            from_email = EMAIL_HOST_USER
            recipient_list = [email]

            send_mail(subject, message, from_email, recipient_list)

            alert.activated = False
            alert.save()
