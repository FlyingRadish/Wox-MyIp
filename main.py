# -*- coding: utf-8 -*-

from wox import Wox
import subprocess
import os

class HelloWorld(Wox):

    def query(self, query):
        (status, out) = subprocess.getstatusoutput("ipconfig |findstr IP")
        lines = out.split("\n")
        results = []
        for line in lines:
            if "IPv4" in line:
                ip = line.split(":")[1].strip()
                results.append({
                "Title": ip,
                "SubTitle": "Copy to clipboard",
                "IcoPath":"Images/app.png",
                'JsonRPCAction': {
                    'method': 'copyToClipboard',
                    'parameters': [ip],
                    'dontHideAfterAction': False
                    }
                })
        return results

    def copyToClipboard(self, value):
        command = 'echo ' + value.strip() + '| clip'
        os.system(command)

if __name__ == "__main__":
    HelloWorld()