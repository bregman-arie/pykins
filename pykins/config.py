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
import ConfigParser
import os


class Config():

    def __init__(self):
        self.load_from_all_sources()

    def load_config_from_env(self):
        """Loads configuration from environment variables."""
        app_envs = filter(
            lambda s: s.startswith(
                '{}_'.format(self.name.upper())), os.environ.keys())
        for env_key in app_envs:
            if os.environ[env_key]:
                self.config[env_key] = os.environ[env_key]

    def load_config_from_file(self):
        """Loads configuration from a file."""
        cfg_parser = ConfigParser()
        cfg_parser.read(
            self.config['{}_CONFIG_FILE'.format(self.name.upper())])

        for section in cfg_parser.sections():
            for key in cfg_parser.options(section):
                k = "{}_%s_%s".format(
                    self.name.upper()) % (section.upper(), key.upper())
                self.config[k] = cfg_parser.get(section, key)

    def load_from_all_sources(self, args):
        """Load configuration from different sources

        Built-in Pykins configuration
        Environment variables which start with PYKINS_ prefix
        """
        for key in dir(Config):
            if key.isupper():
                self.config[key] = getattr(Config, key)

        # Check if user pointed to a different config file from CLI or ENV vars
        if vars(args)['{}_CONFIG_FILE'.format(self.name.upper())]:
            self.config['{}_CONFIG_FILE'.format(self.name.upper())] = vars(
                args)['{}_CONFIG_FILE'.format(self.name.upper())]
        elif '{}_CONFIG_FILE'.format(self.name.upper()) in os.environ:
            self.config['{}_CONFIG_FILE'.format(
                self.name.upper())] = os.environ['{}_CONFIG_FILE'.format(
                    self.name.upper())]

        self.load_config_from_env()
        self.load_config_from_file()
        self.load_config_from_parser(args)

        # Make sure critical configuration is provided
        for k in ['JENKINS_URL', 'JENKINS_USER', 'JENKINS_PASSWORD']:
            if not self.config.get('{}_'.format(self.name.upper()) + k):
                raise exceptions.MissingConfigException(parameter='{}_'.format(
                    self.name.upper()) + k)


    def load_from_all_sources(self, args):
        """Load configuration from different sources

        Built-in Pykins configuration
        Environment variables which start with PYKINS_ prefix
        """
        for key in dir(Config):
            if key.isupper():
                self.config[key] = getattr(Config, key)

        # Check if user pointed to a different config file from CLI or ENV vars
        if vars(args)['{}_CONFIG_FILE'.format(self.name.upper())]:
            self.config['{}_CONFIG_FILE'.format(self.name.upper())] = vars(
                args)['{}_CONFIG_FILE'.format(self.name.upper())]
        elif '{}_CONFIG_FILE'.format(self.name.upper()) in os.environ:
            self.config['{}_CONFIG_FILE'.format(
                self.name.upper())] = os.environ['{}_CONFIG_FILE'.format(
                    self.name.upper())]

        self.load_config_from_env()
        self.load_config_from_file()
        self.load_config_from_parser(args)

        # Make sure critical configuration is provided
        for k in ['JENKINS_URL', 'JENKINS_USER', 'JENKINS_PASSWORD']:
            if not self.config.get('{}_'.format(self.name.upper()) + k):
                raise exceptions.MissingConfigException(parameter='{}_'.format(
                    self.name.upper()) + k)
