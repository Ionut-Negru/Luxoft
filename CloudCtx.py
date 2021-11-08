# CloudCtx.py
"""CloudCTX class"""

import datetime
from HealthInst import HealthInst


def replace_empty_entries(value=""):
    if value == '':
        return '-'
    else:
        return value


class CloudCtx:
    count = 0

    def __init__(self):
        """Initialization of attributes"""
        self.lastModified = None
        self.name = None
        self.tenant_name = None
        self.description = None
        self.name_alias = None
        self.ctx_profile_name = None
        self.HealthInst = None
        CloudCtx.count += 1

    def parse_json(self, json_entry=[]):
        try:
            self.lastModified = datetime.datetime.strptime(json_entry['hcloudCtx']['attributes']['modTs'],
                                                           '%Y-%m-%dT%H:%M:%S.%f%z')
            self.name = replace_empty_entries(json_entry['hcloudCtx']['attributes']['name'])
            self.tenant_name = replace_empty_entries(json_entry['hcloudCtx']['attributes']['tenantName'])
            self.description = replace_empty_entries(json_entry['hcloudCtx']['attributes']['description'])
            self.name_alias = replace_empty_entries(json_entry['hcloudCtx']['attributes']['nameAlias'])
            self.ctx_profile_name = replace_empty_entries(json_entry['hcloudCtx']['attributes']['ctxProfileName'])
            if len(json_entry['hcloudCtx']['children']) > 0:
                self.HealthInst = HealthInst(json_entry['hcloudCtx']['children'][0]['healthInst']['attributes']['cur'],
                                             json_entry['hcloudCtx']['children'][0]['healthInst']['attributes']['maxSev'])
            else:
                self.HealthInst = HealthInst(0)
        except KeyError:
            print("The json entry was invalid")

    @staticmethod
    def check_number_of_entries():
        print(f"There are {CloudCtx.count} entries of cloudCtx")

    def __repr__(self):
        return (f'Name = {self.name} \n' 
                f'Tenant name = {self.tenant_name} \n' 
                f'Health = {self.HealthInst.displayed_health()} \n' 
                f'Description = {self.description} \n' 
                f'Name Alias = {self.name_alias} \n' 
                f'CTX profile name = {self.ctx_profile_name} \n' 
                f'Last modified : {self.lastModified.strftime("%d/%m/%Y %H:%M:%S %p")} \n')

    def __str__(self):
        return repr(self)
