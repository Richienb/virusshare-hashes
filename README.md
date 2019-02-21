# Virus Share Hashes [![Travis Build Status](https://img.shields.io/travis/com/Richienb/virusshare-hashes.svg?style=for-the-badge&logo=travis&label=Travis%20Build)](https://travis-ci.com/Richienb/virusshare-hashes)

Every single [VirusShare](https://virusshare.com/hashes.4n6) MD5 hash in a single file, ready for distribution and CI integrations.

## How to use

### Use the online interface

[ROS Quick Scan](https://richienb.github.io/ros-quick-scan) is an online tool that leverages the [ROS Quick Scan API](#use-the-online-api) to check files.

### Download the pre-created list of MD5 hashes

#### Download URL

Download from this URL:
```
https://media.githubusercontent.com/media/Richienb/virusshare-hashes/master/virushashes.txt
```

#### Using CURL

```sh
curl -L -o virushashes.txt https://media.githubusercontent.com/media/Richienb/virusshare-hashes/master/virushashes.txt
```

#### Using WGET

```sh
wget https://media.githubusercontent.com/media/Richienb/virusshare-hashes/master/virushashes.txt
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
{"safe": true, "success": true}
```

**Example failed output**:

```json
{"success": false, "type": 400, "message": "The q parameter is too short. An MD5 hash is exactly 32 characters long."}
```

## Compile the list of hashes yourself

The hashes are updated weekly but you can manually build the hashes yourself as well.

#### What you need

- Python 2.x or newer.
- An internet connection.
- Available disk space. 5GB (not including Python) should be more than enough; at the time of writing the generated file is only 1.02GB big.

#### How to do it

1. Download the generation file from `https://raw.githubusercontent.com/Richienb/virusshare-hashes/master/generate.py`. 
  
2. Generate the hashes by running `python generate.py`

3. Wait a while

4. You will know that the operation has succeeded when you receive this message in the command line: `Hashes file creation complete.`

## Mirror the hashes file

### What you need

- A new GitHub repository with Travis CI installed

### How to do it

1. Set the following content in your `.travis.yml` file, replacing the marked areas with your own information.

```yml
language:                 generic

before_install:
  - git remote set-url origin https://Richienb:${github_token}@github.com/<REPO_OWNER_USERNAME>/<REPO_NAME>.git
  - git config --global user.name "<NAME OF COMMITER (SOMETHING LIKE: 'Commit Bot')>"
  - git config --global user.email "<COMMITTER EMAIL ADDRESS (THIS COULD BE YOURS)>"
  - echo -e "machine github.com\n  login $github_token" > ~/.netrc
  - git lfs pull

before_script:
  - rm -f virushashes.txt

script:
  - curl -L -o virushashes.txt https://media.githubusercontent.com/media/Richienb/virusshare-hashes/master/virushashes.txt
  
after_script:
  - git add virushashes.txt
  - git commit -m "CI | Updated the hashes library for legacy support [skip ci]"
  - git push
  
notifications: email: false
```

2. [Create](https://github.com/settings/tokens/new) a GitHub personal access token and choose the `public_repo` scope for public repositories or `repo` for private repositories.

3. Set the `github_token` environmental variable in Travis CI to that token.

4. Schedule a cron job with a daily interval, with the option of only running it if one hasn't in the past 24 hours selected.

5. Ensure Git LFS is working properly. If not, run the following command in the repository directory: `git lfs track "virushashes.txt"`
