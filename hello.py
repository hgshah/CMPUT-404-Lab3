#!/usr/bin/env python3
import os
import json
dict = {}
print("Content-Type: text/plain") # http header
print()

dict.update(os.environ)
update = json.dumps(dict) # to JSON
print(update)