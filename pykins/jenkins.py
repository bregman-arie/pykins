# Copyright 2019 Arie Bregman
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
import yaml

LOG = logging.getLogger(__name__)


class Jenkins():
    """Represents Jenkins instance."""

    DEFAULT_CONF_PATH = "/etc/pykins/pykins.yaml"

    def __init__(self, url=None, user=None, token=None):
        """Initialize client."""
        self.url = url
        self.user = user
        self.token = token
        if not all([url, user, token]):
            self.load_configuration()

    def load_configuration(self):
        """Load pykins configuration from a file."""
        with open(self.DEFAULT_CONF_PATH, 'r') as f:
            conf = yaml.load(f)
            for k,v in conf.items():
                self.url = v['url']
                self.user = v['user']
                self.token = v['token']
        LOG.info("Used configuration: {}".format(self.DEFAULT_CONF_PATH))
