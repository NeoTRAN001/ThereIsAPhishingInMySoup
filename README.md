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
$ python3 my_soup.py --help

Options:
  -s, --scam TEXT      Web template name.   python my_soup.py -s Name
  -p, --password TEXT  View action history. python my_soup.py -p True
  -i, --info TEXT      View info tools.     python my_soup.py -i True
  --help               Show this message and exit.

```

To see all web templates:
```
python3 my_soup.py
```

Use a single web template:
```
python3 my_soup.py --scam NAME 
```

## License

MIT © Sherlock Project<br/>
Original Creator - [Neo TRAN](https://github.com/NeoTRAN001)
