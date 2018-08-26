from ..models import *
from . import ApiTenants
from django.conf import settings
import sys,inspect
FileName=((inspect.stack()[0][1]).split('/')[-1]).split('.')[0]


def addUser(self, request, format=None):

    FunctionName = FileName + "-" + sys._getframe().f_code.co_name
    try:
        sendData = {}
        if len(User.objects.all()) == 20:
            sendData['RS'] = "SUCCESS"
            sendData['RV'] = None
        else:
            tenantData = ApiTenants.addTenant(self, request, format=None)
            tenant = Tenants.objects.get(TenantID=int(tenantData['RV']['TenantID']))

            user,created = User.objects.get_or_create(TenantID=tenant, Email=request['Email'])
            if "Name" in request:
                user.Name = request['Name'].title()
            if "Email" in request:
                user.Email = request['Email']
            if "Contact" in request:
                user.Contact = request['Contact']
            if "Address" in request:
                user.Address = request['Address']
            user.save()
            sendData['RS'] = "SUCCESS"
            sendData['RV'] = {"UserID": user.UserID}
        return sendData
    except Exception as e:
        sendData = {}
        sendData['RS'] = "RECORD_NOT_FOUND"
        sendData['RV'] = None
        return sendData

def editUser(self, request, format=None):

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
        tenantData = ApiTenants.addTenant(self, request, format=None)
        tenant = Tenants.objects.get(TenantID=int(tenantData['RV']['TenantID']))

        user = User.objects.get(Email=request['Email'])
        if "Name" in request:
            user.Name = request['Name'].title()
        if "Email" in request:
            user.Email = request['Email']
        if "Contact" in request:
            user.Contact = request['Contact']
        if "Address" in request:
            user.Address = request['Address']
        if "TenantName" in request:
            user.TenantID=tenant
            user.TenantID.TenantName = tenant.TenantName
        user.save()
        sendData['RS'] = "SUCCESS"
        sendData['RV'] = {"UserID": user.UserID}
        return sendData
    except Exception as e:
        sendData = {}
        sendData['RS'] = "RECORD_NOT_FOUND"
        sendData['RV'] = None
        return sendData

def deleteUser(self, request, format=None):

    FunctionName = FileName + "-" + sys._getframe().f_code.co_name
    try:
        sendData = {}
        tenantData = ApiTenants.addTenant(self, request, format=None)
        tenant = Tenants.objects.get(TenantID=int(tenantData['RV']['TenantID']))

        user = User.objects.get(Email=request['Email'])
        user.delete()
        sendData['RS'] = "SUCCESS"
        sendData['RV'] = {"UserID": user.UserID}
        return sendData
    except Exception as e:
        sendData = {}
        sendData['RS'] = "RECORD_NOT_FOUND"
        sendData['RV'] = None
        return sendData


