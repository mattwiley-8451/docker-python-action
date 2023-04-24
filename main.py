#!/usr/bin/env python3
import json
# import requests
import sys
from argsy import Argsy

CLI_ARGS="""
program:
    name: docker-shell-action
    args:
        some_file_path:
            cmd_type: option
            flags: '-f|--some-file-path'
            required: true
        sample_string:
            cmd_type: option
            flags: '-s|--sample-string'
            required: true
"""

def call_artifact_search_api():
    pass

def build_request_body(build_name:str, build_number:str, artifact_repo:str) -> str:
    body_dict = dict(
        buildName=build_name,
        buildNumber=build_number,
        repos=[
            artifact_repo
        ]
    )
    return json.dumps(body_dict)


def main():

    argsy = Argsy(config_str=CLI_ARGS)
    parsed_args = argsy.parse_args(args=sys.argv[1:], print_result=True)

    print(json.dumps(parsed_args.get('args')))
    print(build_request_body("my-build","1.0.123-java","java-dev-local"))



main()