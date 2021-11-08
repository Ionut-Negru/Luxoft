# CloudCtx.py
"""CloudCTX class"""

import datetime
from HealthInst import HealthInst


class CloudCtx:
    count = 0

    def __init__(self, json_entry=()):
        """Initialization of attributes"""

        self.lastModified = datetime.datetime.strptime(json_entry['hcloudCtx']['attributes']['modTs'],
                                                       '%Y-%m-%dT%H:%M:%S.%f%z')
        self.name = json_entry['hcloudCtx']['attributes']['name']
        self.tenant_name = json_entry['hcloudCtx']['attributes']['tenantName']
        self.description = json_entry['hcloudCtx']['attributes']['description']
        self.name_alias = json_entry['hcloudCtx']['attributes']['nameAlias']
        self.ctx_profile_name = json_entry['hcloudCtx']['attributes']['ctxProfileName']
        if len(json_entry['hcloudCtx']['children']) > 0:
            self.HealthInst = HealthInst(json_entry['hcloudCtx']['children'][0]['healthInst']['attributes']['cur'],
                                         json_entry['hcloudCtx']['children'][0]['healthInst']['attributes']['maxSev'])
        else:
            self.HealthInst = HealthInst(0)
        self.check_empty_attributes()

        CloudCtx.count += 1

    def check_empty_attributes(self):
        if self.name == '':
            self.name = '-'
        if self.tenant_name == '':
            self.tenant_name = '-'
        if self.description == '':
            self.description = '-'
        if self.ctx_profile_name == '':
            self.ctx_profile_name = '-'
        if self.name_alias == '':
            self.name_alias = '-'

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
