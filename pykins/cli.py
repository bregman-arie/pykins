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

from pykins.config import Config
from pykins.jenkins import Jenkins
from pykins.common import exceptions
import pykins.parser as pykins_parser

LOG = logging.getLogger(__name__)


class Client():
    """Represents application CLI."""

    def __init__(self, args):
        """Initialize client."""
        self.args = args
        self.config = Config(self.args)
        try:
            self.jenkins = Jenkins(self.config.options['jenkins'],
                                   self.config.options['user'],
                                   self.config.options['password'])
        except KeyError as e:
            raise exceptions.MissingConfigException(e.message)

def main():
    """Main entry for Pykins CLI."""
    # Create parser object & parse arguments provided by the user
    parser = pykins_parser.create_parser()
    args = parser.parse_args()

    # Create Pykins client and execute given command
    pykins_client = Client(args)
    pykins_client.execute()
