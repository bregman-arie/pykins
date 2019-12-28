# Copyright 2017 Infuse Team
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
