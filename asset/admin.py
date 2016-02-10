# coding:utf-8
from django.contrib import admin

## same with from asset.models import Host
from .models import Host


class HostAdmin(admin.ModelAdmin):
    list_display = ('ip', 'open_port', 'status', 'update_time', 'created_time')


admin.site.register(Host, HostAdmin)
