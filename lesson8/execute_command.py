#!/usr/bin/env python
import subprocess
command = "msg * you have been hacked"#Windows command, Linux or OSX
subprocess.Popen(command, shell=True)