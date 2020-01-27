# Copyright 2019 Arie Bregman
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
import crayons


def general_usage():
    """Returns general usage string."""
    message = """
Usage Examples:

    Analyze why a build failed
    $ {}

    List all jobs
    $ {}

    List jobs with substring 'neutron'
    $ {}

""".format(crayons.yellow('pykins build analyze <job_name> <build_number>'),
           crayons.yellow('pykins job list'),
           crayons.yellow('pykins job list neutron'))
    return message
