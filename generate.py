"""

This module is used for generating the file containing all the hashes

"""
from os import remove as rmfile
from urllib.request import urlretrieve
from urllib.error import URLError, HTTPError
from socket import create_connection
from os.path import isfile

# Check for internet connection
print("Checking for an internet connection...")
try:
    create_connection(("www.google.com", 80))
    print("Internet connection established!")
except OSError:
    print("Please connect to the internet!")
    print("Press any key to close...")
    input("")
    exit()

# Clear File
if isfile("virushashes.txt"):
    print("Clearing main file...")
else:
    print("Creating main file...")
open("virushashes.txt", "w").close()
print("Action completed!", end="\n")

# Clear Temporary File
if isfile("newhashes.txt"):
    print("Removing temporary hashes file...")
    print("Action completed!", end="\n")

# Find all possible files
for i in range(0, 99999):
    print("Trying https://virusshare.com/hashes/VirusShare_{0}.md5...".format(
        str(i).zfill(5)))
    try:

        # Try to download file
        urlretrieve(
            "https://virusshare.com/hashes/VirusShare_{0}.md5".format(
                str(i).zfill(5)), "newhashes.txt")
        print("Download success!")
        print("Appending...")

        # Append file - Open hashes file
        with open("virushashes.txt", "r+") as f:
            # Open newly downloaded hashes file
            with open("newhashes.txt", "r") as ff:
                # For each line in the newly downloaded hashes file
                for ii in enumerate(ff.readlines()):
                    # If the current string is not a comment (doesn't start
                    # with #)
                    if not str(ii[1]).startswith("#"):
                        # Write that string to the hashes file
                        f.write(str(ii[1]))

        print("Appending complete!")
        print("Removing temporary file...")

        # Remove temporary file
        rmfile("newhashes.txt")
        print("Operation for file " + str(i).zfill(5) + " complete.", end="\n")

    # Catch HTTP response code
    except HTTPError as e:

        # Check if code is 404
        if e.code == 404:
            print("File " + str(i).zfill(5) + " not found.")
            print("Stopping...")
            break

        # Otherwise raise an error
        else:
            print("An error has occured: Recieved URL response code " + e.code)

            # Exit the execution with a value of 1
            exitexc(1)

    # Catch server error
    except URLError as e:

        # Raise an error
        print("Unable to reach the server: Reason provided is " + str(e.reason))

        # Exit the execution with a value of 1
        exitexc(1)

    # Catch any other exception
    except Exception as exc:

        # Raise an error
        print("ERROR: An error of type {0} occured because {1}".format(
            type(exc).__name__, str(exc.args[0])))

        # Exit the execution with a value of 1
        exitexc(1)

# Notify user of completion
print("Hashes file creation complete.")
