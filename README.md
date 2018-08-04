# Virus Share Hashes [![Build Status](https://travis-ci.com/Richienb/virusshare-hashes.svg?branch=master)](https://travis-ci.com/Richienb/virusshare-hashes)

Every single [VirusShare](https://virusshare.com/hashes.4n6) MD5 hash in a single file, ready for distribution and CI integrations.

## How to use

### Download the pre-created list of MD5 hashes

#### Using CURL

```sh
$ curl -L -o virushashes.txt https://rawgit.com/Richienb/virusshare-hashes/master/virushashes.txt
```

#### Using WGET

```sh
$ wget https://rawgit.com/Richienb/virusshare-hashes/master/virushashes.txt
```

#### Tips

URL not working? Alternate URL: `https://raw.githubusercontent.com/Richienb/virusshare-hashes/master/virushashes.txt`

Other methods of download **are** supported

### Compile the list of hashes yourself

The hashes are updated daily but you can manually build the hashes yourself as well.

#### What you need

- Python 3.x and later (backwards compatibility to Python 2.x is also supported).
- An internet connection (to download the generator).
- Avalible disk space. 10MB should be more than enough; at the time of writing it is only 4.3MB big.

#### How to do it

1. Download the generation file from `https://rawgit.com/Richienb/virusshare-hashes/master/generate.py`. 

    URL not working? Alternate URL: `https://raw.githubusercontent.com/Richienb/virusshare-hashes/master/generate.py`
  
2. Generate the hashes by running `python generate.py`

3. Wait a while

4. You will know that the operation has succeded if you recieve this message in the commandline: `Hashes file creation complete.`
