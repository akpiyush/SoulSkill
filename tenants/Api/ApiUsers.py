from ..models import *
from . import ApiTenants
from django.conf import settings
import sys,inspect
FileName=((inspect.stack()[0][1]).split('/')[-1]).split('.')[0]


def addUser(self, request, format=None):

    FunctionName = FileName + "-" + sys._getframe().f_code.co_name
    if request['Token'] != settings.TOKEN:
        sendData = {}
        sendData['RS'] = "TOKEN_ERROR"
        sendData['RV'] = None
        return sendData
    try:
        sendData = {}
        tenantData = ApiTenants.addTenant(self, request, format=None)
        tenant = Tenants.objects.get(TenantID=int(tenantData['RV']['TenantID']))
        if len(User.objects.filter(TenantID=tenant)) == 20:
            sendData['RS'] = "CANNOT_ADD_USER"
            sendData['RV'] = None
        else:
            
            if len(User.objects.filter(Email=request['Email'])) == 1:
                sendData['RS'] = "EMAIL_ALREADY_EXISTS"
                sendData['RV'] = None
            else:
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
    if request['Token'] != settings.TOKEN:
        sendData = {}
        sendData['RS'] = "TOKEN_ERROR"
        sendData['RV'] = None
        return sendData
    try:
        sendData = {}
        tenantData = ApiTenants.addTenant(self, request, format=None)
        tenant = Tenants.objects.get(TenantID=int(tenantData['RV']['TenantID']))

        user = User.objects.get(Email=request['Email'])
        if "Name" in request:
            user.Name = request['Name'].title()
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
    if request['Token'] != settings.TOKEN:
        sendData = {}
        sendData['RS'] = "TOKEN_ERROR"
        sendData['RV'] = None
        return sendData
    try:
        sendData = {}
        
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

def viewTenentUser(self, request, format=None):

    FunctionName = FileName + "-" + sys._getframe().f_code.co_name
    if request['Token'] != settings.TOKEN:
        sendData = {}
        sendData['RS'] = "TOKEN_ERROR"
        sendData['RV'] = None
        return sendData
    try:
        sendData = {}
        userData = []
        tenant = Tenants.objects.get(TenantName=request['TenantName'])

        user = User.objects.filter(TenantID=tenant)
        for item in user:
            userData.append({"Name":item.Name,"Email":item.Email,"Contact":item.Contact,"Address":item.Address})
        sendData['RS'] = "SUCCESS"
        sendData['RV'] = userData
        return sendData
    except Exception as e:
        sendData = {}
        sendData['RS'] = "RECORD_NOT_FOUND"
        sendData['RV'] = None
        return sendData

