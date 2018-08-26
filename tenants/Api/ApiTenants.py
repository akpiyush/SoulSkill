from ..models import *
from django.conf import settings
import sys,inspect
FileName=((inspect.stack()[0][1]).split('/')[-1]).split('.')[0]

print("**********************************************************************")
def addTenant(self, request, format=None):

    FunctionName = FileName + "-" + sys._getframe().f_code.co_name
    '''if (checkToken(self, request, format=None) == False):
        LoggerDataV1_0.LogDataV1_0(settings.SERVER_TYPE, request['IpAddress'], request['PubIp'], FunctionName,
                                   "Token Error", request)
        sendData = {}
        sendData['RC'] = ErrorCodes.ERROR_CODE_LIST["TOKEN_ERROR"]
        sendData['RS'] = "TOKEN_ERROR"
        sendData['RV'] = None
        return sendData'''
    try:
        sendData = {}
        tenant,created = Tenants.objects.get_or_create(TenantName=request['TenantName'].title())
        tenant.save()
        #sendData['RC'] = ErrorCodes.ERROR_CODE_LIST["SUCCESS"]
        sendData['RS'] = "SUCCESS"
        sendData['RV'] = {"TenantID": tenant.TenantID}
        return sendData
    except Exception as e:
        print(e)
        sendData = {}
        #sendData['RC'] = ErrorCodes.ERROR_CODE_LIST["RECORD_NOT_FOUND"]
        sendData['RS'] = "RECORD_NOT_FOUND"
        sendData['RV'] = None
        return sendData
