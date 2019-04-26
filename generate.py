"""
This module is used for generating the file containing all the hashes

To use it, execute `python generate.py`
"""
from urllib.request import urlopen
from urllib.error import HTTPError
from socket import create_connection
from os.path import isfile
from sys import exit
from readsettings import ReadSettings

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

# Create list for url storage
urls = []

# While the virushashes file is open
with open("virushashes.txt", "a") as f:
    # For each possible file
    for i in range(0, 99999):
        # Set URL to a variable
        url = "https://virusshare.com/hashes/VirusShare_{}.md5".format(
            str(i).zfill(5))
        print("Attemping to download {}...".format(url))

        try:
            # Try to download the file
            with urlopen(url) as resp:
                # Append the URL to the list
                urls.append(url)

                # Write the response to the file
                f.write("\n".join(
                    str(resp.read()).strip("b'").split("\\n")[6:]))

            print("Successfully saved {}.".format(url))

        except HTTPError as e:
            # Check if a 404 was received
            if e.code == 404:
                print("{} returned a 404.".format(url))
                break

# Print completion message
print("Hashes file creation complete.")

# Save urls
ReadSettings("urls.json").json(urls)
