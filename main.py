#!/usr/bin/env python3
import json
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

def main():

    argsy = Argsy(config_str=CLI_ARGS)
    parsed_args = argsy.parse_args(args=sys.argv[1:], print_result=True)

    print(json.dumps(parsed_args.get('args')))

main()