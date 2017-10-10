#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from django.db import models
import datetime

# Create your models here.


class Barrage(models.Model):
    User_name = models.CharField(max_length=64, verbose_name='用户名称')
    User_Barrage = models.TextField(max_length=1024, verbose_name='弹幕内容')
    User_level = models.CharField(max_length=16,verbose_name='用户等级')
    User_Write_back = models.DateTimeField(verbose_name='发言时间',default=datetime.now)

    class Meta:
        db_table = 'Barrage'
        verbose_name = '弹幕表'
        verbose_name_plural = '弹幕表'

    def __str__(self):
        return self.User_name
