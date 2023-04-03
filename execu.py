import os
import base64
counter=0
with open('outfile64.txt') as f:
    for line in f:
        base64_string =line.strip('\n')
        base64_bytes = base64_string.encode("ascii")
        sample_string_bytes = base64.b64decode(base64_bytes)
        sample_string = sample_string_bytes.decode("ascii")
        print('https://'+sample_string+'/')
        os.system('python3.8 51187.py https://'+sample_string+'/')
        print(counter)
        counter +=1


print("fin")
