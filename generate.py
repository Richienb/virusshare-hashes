"""
This module is used for generating the file containing all the hashes

To use it, execute `python generate.py`
"""
from urllib.request import urlopen
from urllib.error import HTTPError
from socket import create_connection
from os.path import isfile
from sys import exit

# Check for an internet connection
try:
    create_connection(("www.google.com", 443))
    print("Internet connection established!")
except OSError:
    print("Please connect to the internet!")
    exit(1)

# Check if hash file exists
if isfile("virushashes.txt"):
    print("Clearing main file...")
else:
    print("Creating main file...")

# Create or clear the hash file
open("virushashes.txt", "w").close()

# While the virushashes file is open
with open("virushashes.txt", "a") as f:
    # For each possible file
    for i in range(0, 99999):
        # Set URL to a variable
        url = "https://virusshare.com/hashes/VirusShare_{0}.md5".format(
            str(i).zfill(5))
        print("Attemping to download " + url + "...")

        try:
            # Try to download the file
            with urlopen(url) as resp:

                # Write the response to the file
                f.write("\n".join(str(resp.read()).strip("b'").split("\\n")))

            print("Successfully saved " + url)

        except HTTPError as e:
            # Check if a 404 was received
            if e.code == 404:
                print(url + " returned a 404.")
                print("Hashes file creation complete.")
                exit(0)
