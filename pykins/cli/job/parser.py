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
import sys

from pykins.job import JenkinsJob


def create_job_parser(client_subparsers, parent_parser):
    """Creates job parser"""
    if not sys.stdin.isatty():
        default_args = sys.stdin.read().splitlines()
        default_nargs = '*'  # when pipeing no args are accepted (empty stdin)
    else:
        default_args = None
        default_nargs = '+'  # without piping, no args would generare error

    job_parser = client_subparsers.add_parser("job", parents=[parent_parser])
    job_action_subparser = job_parser.add_subparsers(title="action",
                                                     dest="job_command")

    # Count
    job_count_parser = job_action_subparser.add_parser(
        "count", help="print number of jobs", parents=[parent_parser])
    job_count_parser.add_argument('string', help='job name or part of it',
                                  nargs='?')

    # List
    job_list_parser = job_action_subparser.add_parser(
        "list", help="list job(s)", parents=[parent_parser])
    job_list_parser.set_defaults(cls=JenkinsJob, func='list')
    job_list_parser.add_argument('name',
                                 nargs='*',
                                 default=default_args,
                                 help='job name or part of it')
    # Delete
    job_delete_parser = job_action_subparser.add_parser(
        "delete", help="delete job", parents=[parent_parser])
    job_delete_parser.add_argument('name',
                                   nargs=default_nargs,
                                   default=default_args,
                                   help='the name of the job(s) to delete')

    # Console Output
    job_output_parser = job_action_subparser.add_parser(
        "output", help="Print job console text", parents=[parent_parser])
    job_output_parser.add_argument('name', help='the name of the job')
    job_output_parser.add_argument('--build', required=False, type=int,
                                   help='build number', dest='build_num')
    job_output_parser.add_argument('--current', action="store_true",
                                   help='Display current build output',
                                   dest='current')

    # Build job
    job_build_parser = job_action_subparser.add_parser(
        "build",
        help="build job",
        parents=[parent_parser])
    job_build_parser.add_argument(
        'name',
        help='the name of the job to build',
        nargs=default_nargs,
        default=default_args)
    job_build_parser.add_argument(
        '-p', '--parameters', type=str, help='params for parameterized job')
    job_build_parser.add_argument(
        '-y', '--params_yml', type=str,
        help='YAML file with params for parameterized job')

    # Copy job
    job_copy_parser = job_action_subparser.add_parser(
        "copy", help="copy job", parents=[parent_parser])
    job_copy_parser.add_argument(
        'source_job_name', help='the name of the job to copy')
    job_copy_parser.add_argument(
        'dest_job_name', help='the name of the new job')
    # Disable job
    job_disable_parser = job_action_subparser.add_parser(
        "disable",
        help="disable job",
        parents=[parent_parser])
    job_disable_parser.add_argument(
        'name',
        help='the name of the job to disable',
        nargs=default_nargs,
        default=default_args)
    # Enable job
    job_enable_parser = job_action_subparser.add_parser(
        "enable", help="enables job", parents=[parent_parser])
    job_enable_parser.add_argument('name',
                                   help='the name of the job to enable',
                                   nargs=default_nargs,
                                   default=default_args)
    # Print information on last build
    job_last_build_parser = job_action_subparser.add_parser(
        "last_build", help="Print information on last build",
        parents=[parent_parser])
    job_last_build_parser.add_argument(
        'name', help='the name of the job')
