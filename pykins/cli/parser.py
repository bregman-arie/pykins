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
import argparse

from pykins.cli.analysis.parser import create_analysis_parser
from pykins.cli.job.parser import create_job_parser


def create_parser():
    """Returns argument parser"""

    # top level parser
    parent_parser = argparse.ArgumentParser(add_help=False)

    main_parser = argparse.ArgumentParser()
    main_parser.add_argument(
        '--debug', '-d', dest="debug",
        help='turn on debug')

    client_subparsers = main_parser.add_subparsers(
        title="client", dest="main_command")

    create_analysis_parser(client_subparsers, parent_parser)
    create_job_parser(client_subparsers, parent_parser)

    return main_parser
