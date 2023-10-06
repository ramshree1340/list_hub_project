# Register your models here.
from django.contrib import admin
from .models import ListHubProperty  # Import your model


class ListHubPropertyAdmin(admin.ModelAdmin):
    list_display = ('address', 'description', 'modified_date')  # Customize the displayed fields


# Register your model using the traditional method
admin.site.register(ListHubProperty, ListHubPropertyAdmin)
