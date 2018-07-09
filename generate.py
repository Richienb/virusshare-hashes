from os import remove as rmfile
import urllib.request
from socket import create_connection

# Check for internet connection
print("Checking for an internet connection...")
try:
    create_connection("www.google.com", 80)
    print("Internet connection established!")
except OSError:
    print("Please connect to the internet!")
    print("Press any key to close...")
    input("")
    exit()

# Clear File
print("Creating/Clearing main file...")
open("virushashes.txt", "w").close()
print("Clearing completed!")

# Find all possible files
for i in range(0, 99999):
    print("Trying " + "https://virusshare.com/hashes/VirusShare_" +
          str(i).zfill(5) + ".md5" + " ...")
    try:
        urllib.request.urlretrieve(
            "https://virusshare.com/hashes/VirusShare_" + str(i).zfill(5) + ".md5", "newhashes.txt")
        print("Download success!")
        print("Appending...")
        with open("virushashes.txt", "r+") as f:
            with open("newhashes.txt", "r") as ff:
                for ii in enumerate(ff.readlines()):
                    while True:
                        f.write(str(ii[1]))
        print("Appending complete!")
        print("Removing temporary file...")
        rmfile("newhashes.txt")
        print("Operation for file " + str(i).zfill(5) + " complete.")
    except urllib.request.URLError:
        if e.code == 404:
            break
        else:
            raise RunTimeError(
                "An error has occured: Recieved URL response code " + e.code)
