# Copyright 2018 Arie Bregman
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


class PykinsException(Exception):
    """Base Pykins Exception.

    To use this class, inherit from it and define a 'message' property.
    """
    message = "An unknown exception occurred."

    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            self.message = args[0]
        super(PykinsException, self).__init__(self.message % kwargs)
        self.msg = self.message % kwargs


class APIException(PykinsException):
    message = "Something, somewhere went terribly wrong"


class MissingConfigException(PykinsException):
    message = "You forget to specify critical parameter: %(parameter)s"
