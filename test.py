import os
import subprocess

command_second = "date '+%S'"
a = 1


while a == 1:
    value = subprocess.check_output(command_second, shell=True)
    #print(value,type(value))
    value = int(value)
    if value == 00:
        print("Done")
        continue
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")
        
