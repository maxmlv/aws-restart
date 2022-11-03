import os
import subprocess

os.system("ls")
subprocess.run(["ls", "-l", "sys-admin.py"])

command = "uname"
command_argument = "-a"
print(f'Gathering system information with command: {command} {command_argument}')
subprocess.run([command, command_argument])

command = "ps"
command_argument = "-x"
print(f'Gathering active process information with command: {command} {command_argument}')
subprocess.run([command, command_argument])