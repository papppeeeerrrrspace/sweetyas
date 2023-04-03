import os
import base64
def base64_to_string():
    with open('outfile64.txt') as f:
        for line in f:
            with open('result.txt', 'a') as file:
                base64_string =line.strip('\n')
                base64_bytes = base64_string.encode("ascii")
                sample_string_bytes = base64.b64decode(base64_bytes)
                sample_string = sample_string_bytes.decode("ascii")
                file.write(sample_string+'\n')
            file.close()

with open('3.txt') as f:
    for line in f:
        os.system('python 51187.py --url https://'+line.strip('\n')+'/')


print("fin")
