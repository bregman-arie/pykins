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
import logging
import re
import requests
from requests.auth import HTTPBasicAuth

from pykins.jenkins import Jenkins

LOG = logging.getLogger(__name__)


class JenkinsBuild(Jenkins):

    def __init__(self):
        super(JenkinsBuild, self).__init__()

    def analyze(self, args=None):
        """..."""
        console_text_url = "%s/job/%s/lastBuild/consoleText" % (
            self.url, args.job)
        LOG.info("Getting data from: %s" % console_text_url)
        console_output = self.get_text(console_text_url)
        err_output = self.get_errors(console_output)
        print(*err_output, sep="\n")

    def get_errors(self, text):
        errors = []
        linesBeforeMatch = []
        log_urls = []
        for i, l in enumerate(text):
            linesBeforeMatch.append(l)
            # Check if line contains error
            match = re.findall(r'failed=1|fatal|shit', l)
            urls_match = re.findall(r'http.*.log', l)
            if urls_match:
                log_urls.append(urls_match[0])
            if match:
                errors.extend(linesBeforeMatch[-5:])
                # Take extra lines after the match
                for ext_l in text[i + 1:i + 15]:
                    errors.append(ext_l)
        if not errors:
            for url in log_urls[::-1]:
                text = self.get_text(url)
                ext_errors = self.get_errors(text)
                errors.extend(ext_errors)
        return errors

    def get_text(self, req):
        req = requests.get(
            req, verify=False,
            auth=HTTPBasicAuth(self.user, self.token))
        return req.text.split('\n')
