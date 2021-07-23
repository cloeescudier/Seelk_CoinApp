from app.models import User, ValueAlert, PercentageAlert
from django.contrib import admin

# Register your models here.

#admin.site.register(User)
#admin.site.register(ValueAlert)
#admin.site.register(PercentageAlert)


class ValueAlertInline(admin.TabularInline):

    model = ValueAlert
    extra = 0

class PercentageAlertInline(admin.TabularInline):

    model = PercentageAlert
    extra = 0

@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = ('name', 'creation_date', 'email')
    inlines = (ValueAlertInline, PercentageAlertInline,)

@admin.register(ValueAlert)
class ValueAlertAdmin(admin.ModelAdmin):

    list_display = ('name', 'message', 'creation_date', 'activated', 'user', 'value', 'crypto', 'currency', 'direction')

@admin.register(PercentageAlert)
class PercentageAlertAdmin(admin.ModelAdmin):

    list_display = ('name', 'message', 'creation_date', 'activated', 'user', 'timeframe', 'percentage', 'direction')
