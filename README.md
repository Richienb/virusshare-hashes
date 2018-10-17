# Virus Share Hashes [![Travis Build Status](https://img.shields.io/travis/com/Richienb/virusshare-hashes.svg?style=for-the-badge&logo=travis&label=Travis%20Build)](https://travis-ci.com/Richienb/virusshare-hashes)

Every single [VirusShare](https://virusshare.com/hashes.4n6) MD5 hash in a single file, ready for distribution and CI integrations.

## How to use

### Download the pre-created list of MD5 hashes

#### Download URL

Download from this URL:
```
https://rawgit.com/Richienb/virusshare-hashes/master/virushashes.txt
```

Alternatively, as a fallback you can use:
```
https://raw.githubusercontent.com/Richienb/virusshare-hashes/master/virushashes.txt
```

#### Using CURL

```sh
$ curl -L -o virushashes.txt https://rawgit.com/Richienb/virusshare-hashes/master/virushashes.txt
```

#### Using WGET

```sh
$ wget https://rawgit.com/Richienb/virusshare-hashes/master/virushashes.txt
```

Other methods of download **are** supported

### Compile the list of hashes yourself

The hashes are updated daily but you can manually build the hashes yourself as well.

#### What you need

- Python 2.x or newer.
- An internet connection.
- Avalible disk space. 10MB (not including Python) should be more than enough; at the time of writing the generated file is only 4.13MB big.

#### How to do it

1. Download the generation file from `https://rawgit.com/Richienb/virusshare-hashes/master/generate.py`. 

    URL not working? Alternate URL: `https://raw.githubusercontent.com/Richienb/virusshare-hashes/master/generate.py`
  
2. Generate the hashes by running `python generate.py`

3. Wait a while

4. You will know that the operation has succeeded when you receive this message in the command line: `Hashes file creation complete.`
