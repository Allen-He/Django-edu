# _*_ coding: utf-8 _*_
__author__ = 'htt'
__date__ = '$DATE $TIME'

import xadmin
from .models import EmailVerifyRecord

class EmailVerifyRecordAdmin(object):
    pass

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)