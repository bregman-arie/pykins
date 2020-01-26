# Copyright 2020 Arie Bregman
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by selflicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
import crayons
import requests
from requests.auth import HTTPBasicAuth

from pykins.jenkins import Jenkins


class JenkinsJob(Jenkins):

    def __init__(self):
        super(JenkinsJob, self).__init__()

    def list(self, args=None):
        print("listing")
        jobs_url = "%s/api/json" % self.url
        r = requests.get(jobs_url, verify=False,
                         auth=HTTPBasicAuth(self.user, self.token))
        for job in r.json()["jobs"]:
            if 'color' in job:
                if job['color'] == 'red':
                    print(crayons.red(job['name']))
                elif job['color'] == 'yellow':
                    print(crayons.yellow(job['name']))
                elif job['color'] == 'blue':
                    print(crayons.green(job['name']))
                elif job['color'] == 'notbuilt':
                    print(job['name'])
            else:
                print(job['name'])
