from rest_framework import routers
from rest_framework.schemas import views

from .views import ValueAlertViewSet, PercentageAlertViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('values', ValueAlertViewSet)
router.register('percentages', PercentageAlertViewSet)
router.register('users', UserViewSet)