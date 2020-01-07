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
import sys


def create_build_parser(client_subparsers, parent_parser):
    """Creates build parser"""
    build_parser = client_subparsers.add_parser("build",
                                                parents=[parent_parser])
    build_action_subparser = build_parser.add_subparsers(title="action",
                                                         dest="build_command")

    # Analyze build
    build_analyze_parser = build_action_subparser.add_parser(
        "analyze",
        help="analyze a given build",
        parents=[parent_parser])
    build_analyze_parser.add_argument("--number", "-b",
                                      dest="build_number",
                                      required=False,
                                      help='build number')
    build_analyze_parser.add_argument('--name', '-j', dest="job_name",
                                      required=False,
                                      help='job name', nargs=1)
    build_analyze_parser.add_argument('--url', '-u', dest="build_url",
                                      required=False,
                                      help="build URL", nargs=1)

    # Stop build
    build_stop_parser = build_action_subparser.add_parser(
        "stop",
        help="stop a given build",
        parents=[parent_parser])
    build_stop_parser.add_argument("--number", "-b",
                                   dest="build_number",
                                   required=False,
                                   help='build number')
    build_stop_parser.add_argument('--name', '-j', dest="job_name",
                                   required=True,
                                   help='job name', nargs=1)


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


def create_view_parser(client_subparsers, parent_parser):
    """Creates view parser"""

    view_parser = client_subparsers.add_parser("view", parents=[parent_parser])
    view_action_subparser = view_parser.add_subparsers(title="action",
                                                       dest="view_command")

    # View sub-commands

    # List views
    view_list_parser = view_action_subparser.add_parser(
        "list", help="list view(s)", parents=[parent_parser])
    view_list_parser.add_argument('name', help='view name or part of it',
                                  nargs='?')

    # Delete view
    view_delete_parser = view_action_subparser.add_parser(
        "delete", help="delete view", parents=[parent_parser])
    view_delete_parser.add_argument('name',
                                    help='the name of the view to delete')

    # Jobs under a specific view
    view_jobs_parser = view_action_subparser.add_parser(
        "jobs",
        help="List all the jobs under specific view", parents=[parent_parser])
    view_jobs_parser.add_argument(
        'name', help='the name of the view')

    # Create view
    view_create_parser = view_action_subparser.add_parser(
        "create", help="create view", parents=[parent_parser])
    view_create_parser.add_argument(
        'name', help='name of the view', nargs='?')

    # Rename view
    view_rename_parser = view_action_subparser.add_parser(
        "rename", help="rename view", parents=[parent_parser])
    view_rename_parser.add_argument(
        'name', help='the current name of the view')
    view_rename_parser.add_argument(
        'new_name', help='the new name of the view')


def create_node_parser(client_subparsers, parent_parser):
    """Creates node parser"""

    # Node parser
    node_parser = client_subparsers.add_parser("node", parents=[parent_parser])
    node_action_subparser = node_parser.add_subparsers(title="action",
                                                       dest="node_command")

    # Node sub-commands

    # List nodes
    node_list_parser = node_action_subparser.add_parser(
        "list", help="list node(s)", parents=[parent_parser])
    node_list_parser.add_argument('name', help='node name or part of it',
                                  nargs='?')

    # Delete node
    node_delete_parser = node_action_subparser.add_parser(
        "delete", help="delete node", parents=[parent_parser])
    node_delete_parser.add_argument('name',
                                    help='the name of the node to delete')

    # Create node
    node_create_parser = node_action_subparser.add_parser(
        "create", help="create node", parents=[parent_parser])
    node_create_parser.add_argument('name',
                                    help='The name of the node')
    node_create_parser.add_argument('--description', default=None,
                                    required=False,
                                    help='The description of the node')
    node_create_parser.add_argument('--remotefs', default="/var/lib/jenkins",
                                    help='Remote filesystem location to use')
    node_create_parser.add_argument('--labels', default=None,
                                    help='Labels to associate with node')
    node_create_parser.add_argument('--exclusive', type=bool, default=False,
                                    help='Use this node for tied jobs only')
    node_create_parser.add_argument('--executors', type=int, default=2,
                                    help='The number of executors')

    # Info on node
    node_info_parser = node_action_subparser.add_parser(
        "info", help="Print info on node", parents=[parent_parser])
    node_info_parser.add_argument('name', help='the name of the node')


def create_plugin_parser(client_subparsers, parent_parser):
    """Creates plugin parser"""

    # Plugin parser
    plugin_parser = client_subparsers.add_parser("plugin",
                                                 parents=[parent_parser])
    plugin_action_subparser = plugin_parser.add_subparsers(
        title="action", dest="plugin_command")

    # Plugin sub-commands
    plugin_action_subparser.add_parser(
        "list", help="list plugin(s)", parents=[parent_parser])

    plugin_info_parser = plugin_action_subparser.add_parser(
        "info", help="Print information on specified plugin",
        parents=[parent_parser])
    plugin_info_parser.add_argument('name', help='the plugin name',
                                    nargs=1)


def create_parser():
    """Returns argument parser"""

    # Jcli top level parser
    parent_parser = argparse.ArgumentParser(add_help=False)

    main_parser = argparse.ArgumentParser()
    main_parser.add_argument(
        '--config', '-c', dest="PYKINS_CONFIG_FILE",
        help='configuration file')

    client_subparsers = main_parser.add_subparsers(
        title="client", dest="main_command")

    create_job_parser(client_subparsers, parent_parser)
    create_build_parser(client_subparsers, parent_parser)
    create_view_parser(client_subparsers, parent_parser)
    create_node_parser(client_subparsers, parent_parser)
    create_plugin_parser(client_subparsers, parent_parser)

    return main_parser
