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
        """List jobs."""
        jobs_url = "%s/api/json" % self.url
        req = requests.get(
            jobs_url, verify=False,
            auth=HTTPBasicAuth(self.user, self.token))
        jobs = req.json()["jobs"]
        if args.substrings:
            jobs = [job for job in jobs if any(
                substr in job['name'] for substr in args.substrings)]
        self.print_colorized_jobs(jobs)

    @staticmethod
    def print_colorized_jobs(jobs):
        """Job is a dictionary like this:
            {"_class":"hudson.model.FreeStyleProject",
             "name":"util-slave-janitor",
             "url":"https://my_jenkins.com/job/util-slave-janitor/",
             "color":"red"}
        """
        for job in jobs:
            if 'color' in job:
                if job['color'] == 'red':
                    print("{} | {}".format(crayons.red(job['name']),
                                           crayons.red("Failed")))
                elif job['color'] == 'yellow':
                    print("{} | {}".format(crayons.yellow(job['name']),
                                           crayons.yellow("Unstable")))
                elif job['color'] == 'blue':
                    print("{} | {}".format(crayons.green(job['name']),
                                           crayons.green("Passed")))
                elif job['color'] == 'notbuilt':
                    print("{} | {}".format(job['name'], "No Builds"))
            else:
                print(job['name'])
