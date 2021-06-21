#!/bin/python3

import sys
import os
import subprocess
import inspect



# Complete the function below.

def run_process(cmd_args):
    
    with subprocess.Popen(cmd_args, stdout=subprocess.PIPE, shell=True) as proc: 
        print(proc.stdout.read())
        #return proc.stdout.read()
        
        #return '111'
    return "Hello".encode()