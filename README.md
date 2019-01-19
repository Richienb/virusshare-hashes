# Virus Share Hashes [![Travis Build Status](https://img.shields.io/travis/com/Richienb/virusshare-hashes.svg?style=for-the-badge&logo=travis&label=Travis%20Build)](https://travis-ci.com/Richienb/virusshare-hashes)

Every single [VirusShare](https://virusshare.com/hashes.4n6) MD5 hash in a single file, ready for distribution and CI integrations.

## How to use

### Download the pre-created list of MD5 hashes

#### Download URL

Download from this URL:
```
https://raw.githubusercontent.com/Richienb/virusshare-hashes/master/virushashes.txt
```

#### Using CURL

```sh
curl -L -o virushashes.txt https://raw.githubusercontent.com/Richienb/virusshare-hashes/master/virushashes.txt
```

#### Using WGET

```sh
wget https://raw.githubusercontent.com/Richienb/virusshare-hashes/master/virushashes.txt
```

Other methods of download **are** supported

### Use the online API

You can use the ROS Quick Scan API to check if a MD5 hash matches one in the list

**Endpoint**: `https://script.google.com/macros/s/AKfycbyS0v38UlKkLe18CwwxLjxKpQ1CQIUiBZGXvA519W2Pf_nqKmM/exec`

**Type**: `GET`

**Parameters**:

`q`: The MD5 hash to check.

`callback`: An optional JSONP callback.

**Example output**:

```json
{safe: true, success: true}
```

**Example failed output**:

```json
{success: false, type: 400, message: "The q parameter is too short. An MD5 hash is exactly 32 characters long."}
```

### Compile the list of hashes yourself

The hashes are updated weekly but you can manually build the hashes yourself as well.

#### What you need

- Python 2.x or newer.
- An internet connection.
- Avalible disk space. 10MB (not including Python) should be more than enough; at the time of writing the generated file is only 4.13MB big.

#### How to do it

1. Download the generation file from `https://raw.githubusercontent.com/Richienb/virusshare-hashes/master/generate.py`. 
  
2. Generate the hashes by running `python generate.py`

3. Wait a while

4. You will know that the operation has succeeded when you receive this message in the command line: `Hashes file creation complete.`
