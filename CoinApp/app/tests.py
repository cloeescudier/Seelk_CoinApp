from datetime import date, datetime
import datetime
from django.test import TestCase

from app.models import User, ValueAlert, PercentageAlert

# Create your tests here.

class UserTestCase(TestCase):

    def setUp(self):

        self.user = User()
        self.user.name = "User Test"
        self.user.creation_date = date.today()
        self.user.email = "test@gmail.com"
        self.user.save()

    def test_create_user(self):
       
        nb_users_before_add = User.objects.count()

        new_user = User()
        new_user.name = "John Doe"
        new_user.creation_date = date.today()
        new_user.email = "john.doe@gmail.com"
        new_user.save()

        nb_users_after_add = User.objects.count()

        self.assertTrue(nb_users_after_add == nb_users_before_add + 1)

    def test_update_user(self):

        new_name = "Changed"
        self.user.name = new_name
        self.user.save()
        
        temp = User.objects.get(pk=self.user.pk)
        self.assertEqual(self.user.name, new_name)

    def test_delete_user(self):

        nb_users_before_delete = User.objects.count()
        self.user.delete()
        nb_users_after_delete = User.objects.count()

        self.assertTrue(nb_users_after_delete == nb_users_before_delete - 1)

class AlertTestCase(TestCase):

    def setUp(self):

        self.user = User()
        self.user.name = "User Test"
        self.user.creation_date = date.today()
        self.user.email = "test@gmail.com"
        self.user.save()

        self.value_alert = ValueAlert()
        self.value_alert.name = "Value Alert Test"
        self.value_alert.message = "test"
        self.value_alert.creation_date = date.today()
        self.value_alert.activated = True
        self.value_alert.user = self.user
        self.value_alert.value = 5000
        self.value_alert.crypto = "BTC"
        self.value_alert.currency = "USD"
        self.value_alert.direction = "A"
        self.value_alert.save()

        self.percentage_alert = PercentageAlert()
        self.percentage_alert.name = "Percentage Alert Test"
        self.percentage_alert.message = "test"
        self.percentage_alert.creation_date = date.today()
        self.percentage_alert.activated = True
        self.percentage_alert.user = self.user
        self.percentage_alert.timeframe = datetime.timedelta(days=15)
        self.percentage_alert.percentage = 3
        self.percentage_alert.direction = "U"
        self.percentage_alert.save()

    def test_create_value_alert(self):
       
        nb_value_alert_before_add = ValueAlert.objects.count()

        new_alert = ValueAlert()
        new_alert.name = "Test Alert"
        new_alert.message = "test"
        new_alert.creation_date = date.today()
        new_alert.activated = True 
        new_alert.user = self.user

        new_alert.value = 5000
        new_alert.crypto = "BTC"
        new_alert.currency = "USD"
        new_alert.direction = "A"
        new_alert.save()

        nb_value_alert_after_add = ValueAlert.objects.count()

        self.assertTrue(nb_value_alert_after_add == nb_value_alert_before_add + 1)

    def test_update_value_alert(self):

        new_name = "Changed"
        self.value_alert.name = new_name
        self.value_alert.save()
        
        temp = ValueAlert.objects.get(pk=self.value_alert.pk)
        self.assertEqual(self.value_alert.name, new_name)

    def test_delete_value_alert(self):

        nb_value_alert_before_delete = ValueAlert.objects.count()
        self.value_alert.delete()
        nb_value_alert_after_delete = ValueAlert.objects.count()

        self.assertTrue(nb_value_alert_after_delete == nb_value_alert_before_delete - 1)

    def test_create_percentage_alert(self):
       
        nb_percentage_alert_before_add = PercentageAlert.objects.count()

        new_alert = PercentageAlert()
        new_alert.name = "Test Alert"
        new_alert.message = "test"
        new_alert.creation_date = date.today()
        new_alert.activated = True 
        new_alert.user = self.user

        new_alert.timeframe = datetime.timedelta(days=7)
        new_alert.percentage = 5
        new_alert.direction = "U"
        new_alert.save()

        nb_percentage_alert_after_add = PercentageAlert.objects.count()

        self.assertTrue(nb_percentage_alert_after_add == nb_percentage_alert_before_add + 1)

    def test_update_percentage_alert(self):

        new_name = "Changed"
        self.percentage_alert.name = new_name
        self.percentage_alert.save()
        
        temp = PercentageAlert.objects.get(pk=self.percentage_alert.pk)
        self.assertEqual(self.percentage_alert.name, new_name)

    def test_delete_percentage_alert(self):

        nb_percentage_alert_before_delete = PercentageAlert.objects.count()
        self.percentage_alert.delete()
        nb_percentage_alert_after_delete = PercentageAlert.objects.count()

        self.assertTrue(nb_percentage_alert_after_delete == nb_percentage_alert_before_delete - 1)