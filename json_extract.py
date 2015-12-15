import json
import sys

try:
        with open(sys.argv[1], 'r') as jfile:
                j_obj = json.loads(jfile.read())
                print(j_obj['main'])
except IOError:
        pass # silent failure
