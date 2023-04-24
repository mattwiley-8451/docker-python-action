#!/usr/bin/env python3
import json
import sys
from argsy import Argsy

# NOTE: Order of the 'args' is important here. This order must match the order 
# of the args defined in the action.yml run.args list
CLI_ARGS="""
program:
    name: docker-shell-action
    args:
        some_file_path:
            cmd_type: position
            required: true
        sample_string:
            cmd_type: position
            required: true
"""

def main():
    argsy = Argsy(config_str=CLI_ARGS)
    parsed_args = argsy.parse_args(args=sys.argv[1:]).get('args')
    print(json.dumps(parsed_args))

main()