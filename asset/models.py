# coding:utf-8

from django.db import models


class Host(models.Model):
    STATUS_ITEMS = (
        (1, "空闲"),
        (2, "使用中"),
        (3, "报废"),
    )
    ip = models.GenericIPAddressField(verbose_name="主机IP")
    open_port = models.CharField(max_length=1000, verbose_name="开放端口")
    status = models.IntegerField(choices=STATUS_ITEMS, verbose_name="主机状态")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name_plural = "主机"
