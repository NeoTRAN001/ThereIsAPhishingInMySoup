<p align=center>

  <img src="https://github.com/NeoTRAN001/ThereIsAPhishingInMySoup/blob/master/Data/img/logo.png"/>

  <br>
  <span>There is a phishing in my soup, it is a scam tool with <a href="https://github.com/theyahya/sherlock/blob/master/sites.md">phishing</a></span>
  <br><br>
  <a target="_blank" href="https://www.python.org/downloads/" title="Python version"><img src="https://img.shields.io/badge/python-%3E=_3.6-green.svg"></a>
  <a target="_blank" href="LICENSE" title="License: MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
  <a target="_blank" href="https://github.com/NeoTRAN001/ThereIsAPhishingInMySoup/actions" title="Test Status"><img src="https://github.com/sherlock-project/sherlock/workflows/Tests/badge.svg?branch=master"></a>
  <a target="_blank" href="/"><img alt="docker image" src="https://images.microbadger.com/badges/version/theyahya/sherlock.svg"></a>
</p>

<p align="center">
  <a href="#legal-disclaimer">Legal disclaimer</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#installation">Installation</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#usage">Usage</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
</p>

<p align="center">
<a href="https://asciinema.org/a/223115">
<img src="https://github.com/NeoTRAN001/ThereIsAPhishingInMySoup/blob/master/Data/img/Title.png"/>
</a>
</p>

## Legal disclaimer

Usage of BlackEye for attacking targets without prior mutual consent is illegal. It's the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program. Only use for educational purposes.

## Installation

**NOTE**: Python 3.6 or higher is required.

```bash
# clone the repo
$ git clone https://github.com/NeoTRAN001/ThereIsAPhishingInMySoup.git

# change the working directory to sherlock
$ cd ThereIsAPhishingInMySoup

# install python3 and python3-pip if they are not installed

# install the requirements
$ python3 -m pip install -r requirements.txt
```

[![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/NeoTRAN001/ThereIsAPhishingInMySoup&tutorial=README.md)

## Usage

```bash
$ python3 sherlock --help
usage: sherlock [-h] [--version] [--verbose] [--rank]
                [--folderoutput FOLDEROUTPUT] [--output OUTPUT] [--tor]
                [--unique-tor] [--csv] [--site SITE_NAME] [--proxy PROXY_URL]
                [--json JSON_FILE] [--timeout TIMEOUT] [--print-found]
                [--no-color] [--browse]
                USERNAMES [USERNAMES ...]

Sherlock: Find Usernames Across Social Networks (Version 0.12.2)

positional arguments:
  USERNAMES             One or more usernames to check with social networks.

optional arguments:
  -h, --help            show this help message and exit
  --version             Display version information and dependencies.
  --verbose, -v, -d, --debug
                        Display extra debugging information and metrics.
  --rank, -r            Present websites ordered by their Alexa.com global
                        rank in popularity.
  --folderoutput FOLDEROUTPUT, -fo FOLDEROUTPUT
                        If using multiple usernames, the output of the results
                        will be saved to this folder.
  --output OUTPUT, -o OUTPUT
                        If using single username, the output of the result
                        will be saved to this file.
  --tor, -t             Make requests over Tor; increases runtime; requires
                        Tor to be installed and in system path.
  --unique-tor, -u      Make requests over Tor with new Tor circuit after each
                        request; increases runtime; requires Tor to be
                        installed and in system path.
  --csv                 Create Comma-Separated Values (CSV) File.
  --site SITE_NAME      Limit analysis to just the listed sites. Add multiple
                        options to specify more than one site.
  --proxy PROXY_URL, -p PROXY_URL
                        Make requests over a proxy. e.g.
                        socks5://127.0.0.1:1080
  --json JSON_FILE, -j JSON_FILE
                        Load data from a JSON file or an online, valid, JSON
                        file.
  --timeout TIMEOUT     Time (in seconds) to wait for response to requests.
                        Default timeout of 60.0s.A longer timeout will be more
                        likely to get results from slow sites.On the other
                        hand, this may cause a long delay to gather all
                        results.
  --print-found         Do not output sites where the username was not found.
  --no-color            Don't color terminal output
  --browse, -b          Browse to all results on default bowser.
```

To search for only one user:
```
python3 sherlock user123
```

To search for more than one user:
```
python3 sherlock user1 user2 user3
```

Accounts found will be stored in an individual text file with the corresponding username (e.g ```user123.txt```).

## License

MIT © Sherlock Project<br/>
Original Creator - [Siddharth Dushantha](https://github.com/sdushantha)
