from ..models import *
from django.conf import settings
import sys,inspect
FileName=((inspect.stack()[0][1]).split('/')[-1]).split('.')[0]

def addTenant(self, request, format=None):

    FunctionName = FileName + "-" + sys._getframe().f_code.co_name
    if request['Token'] != settings.TOKEN:
        sendData = {}
        sendData['RS'] = "TOKEN_ERROR"
        sendData['RV'] = None
        return sendData
    try:
        sendData = {}
        tenant,created = Tenants.objects.get_or_create(TenantName=request['TenantName'].title())
        tenant.save()
        sendData['RS'] = "SUCCESS"
        sendData['RV'] = {"TenantID": tenant.TenantID}
        return sendData
    except Exception as e:
        sendData = {}
        sendData['RS'] = "RECORD_NOT_FOUND"
        sendData['RV'] = None
        return sendData
