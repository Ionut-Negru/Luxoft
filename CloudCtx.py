# CloudCtx.py
"""CloudCTX class"""
import datetime

from HealthInst import HealthInst
class CloudCtx:
    count = 0
    def __init__(self, name="", tenant_name="", description="", name_alias="", ctx_profile_name="", HealthInst="",last_modified=""):
        """Initialization of attributes"""
        self.name = name
        self.tenant_name = tenant_name
        self.description = description
        self.name_alias = name_alias
        self.ctx_profile_name = ctx_profile_name
        self.HealthInst = HealthInst
        self.lastModified = last_modified
        CloudCtx.count += 1

    def __repr__(self):
        empty = lambda x: '-' if x == "" else x
        straux =  "Name = "+empty(self.name)+"\n"+"Tenant name = "+empty(self.tenant_name)+"\n"+"Health = " +self.HealthInst.displayed_health()+"\n"+"Description = "+empty(self.description)+"\n"+"Name alias = "+empty(self.name_alias)+"\n"+"CTX profile name = "+empty(self.ctx_profile_name)
        if(self.lastModified.hour > 12):
            aux = self.lastModified
            aux = self.lastModified - datetime.timedelta(hours=12)
            return straux + "\n" + "Last modified : " + str(aux.day) + "/" + str(aux.month) + "/" + str(aux.year) + " " + str(aux.hour) + ":" + str(aux.minute) + ":"+ str(aux.second) +" PM"
        else:
            return straux + "\n" + "Last modified : " + str(self.lastModified.day) + "/" + str(
                self.lastModified.month) + "/" + str(self.lastModified.year) + " " + str(
                self.lastModified.hour) + ":" + str(self.lastModified.minute) + ":" + str(
                self.lastModified.second) + " AM"

    def __str__(self):
        return (repr(self))