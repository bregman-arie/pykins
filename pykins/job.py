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
import logging
import re
import requests
from requests.auth import HTTPBasicAuth

from pykins.jenkins import Jenkins

LOG = logging.getLogger(__name__)


class JenkinsJob(Jenkins):

    def __init__(self):
        super(JenkinsJob, self).__init__()

    def count(self, args=None):
        """Count the number of jobs."""
        jobs_url = "%s/api/json" % self.url
        req = requests.get(
            jobs_url, verify=False,
            auth=HTTPBasicAuth(self.user, self.token))
        jobs = req.json()["jobs"]
        LOG.info("Number of jobs: {}".format(len(jobs)))

    def list(self, args=None):
        """List jobs."""
        jobs_url = "%s/api/json" % self.url
        req = requests.get(
            jobs_url, verify=False,
            auth=HTTPBasicAuth(self.user, self.token))
        jobs = req.json()["jobs"]
        if args.substrings:
            if args.re:
                matched_jobs = [job for job in jobs if any(
                    bool((re.compile(substr)).match(
                        job['name'])) for substr in args.substrings)]
            else:
                matched_jobs = jobs = [job for job in jobs if any(
                    substr in job['name'] for substr in args.substrings)]
            job_str = "{} | {}"
            if args.with_links:
                job_str = job_str + " | {}"
            if matched_jobs:
                for job in matched_jobs:
                    LOG.info(job_str.format(
                        job['name'],
                        self.get_result_from_color(job['color']), job['url']))
            else:
                LOG.info(crayons.cyan("Alfred: I'm sorry sir, I couldn't \
find any match"))

    def show(self, args):
        job_url = "%s/job/%s/api/json" % (self.url, args.job)
        req = requests.get(
            job_url, verify=False,
            auth=HTTPBasicAuth(self.user, self.token))
        job = req.json()
        print("Job: {}".format(job['fullName']))
        print("============================\nDescription: {}".format(
            job['description']))
        print("============================\nBuilds:")
        for build in job['builds']:
            print("{} | {} | {}".format(
                build['number'], build['url'],
                build.get('color', crayons.red("Failed"))))

    @staticmethod
    def get_result_from_color(color):
        if color == 'red':
            return crayons.red("Failed")
        elif color == 'yellow':
            return crayons.yellow("Unstable")
        elif color == 'blue':
            return crayons.green("Passed")
        elif color == 'notbuilt':
            return "No Builds"
        else:
            return "Unknown"
