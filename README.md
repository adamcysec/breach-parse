# breach-parse.py

## Synposis
The same [breach-parse](https://github.com/hmaverickadams/breach-parse) tool from [hmaverickadams](https://github.com/hmaverickadams) but written in python3.

## Description
This tool runs about a minute faster than it's bash counterpart and is more accurate when searching. 

The bash version uses `grep -a -E "$1" "$file"` for searches. The `-E` enables extended regex comparision, therefore if your search term is `@bob.com` you can potentially get false positives such as `@bobscom.com`. This tool uses python's `in` keyword for an exact string comparision. 

The bash version splits user and password pairs on `:` , however the dataset also uses `;` for some pairs.

## Installation
Download breached password list from magnet located here: 
```
magnet:?xt=urn:btih:7ffbcd8cee06aba2ce6561688cf68ce2addca0a3&dn=BreachCompilation&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fglotorrents.pw%3A6969&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337
```

I recommend editing line 24 and adding your `BreachCompilation/data` directory as the default `datafile` value or you will need to use the `datafile` parameter:

`py breach-parse.py @yahoo.com yahoo --datafile "/media/adam/BreachCompilation/data"`

## Usage

**Parameter term**
- positional : position 1
- required
- type : str
- one string to search with

**Parameter output**
- positional : position 2
- required
- type : str
- filename to output

**Parameter --datafile, -d**
- type : str
- filepath to BreachCompilation/data

**Parameter --userfile, -u**
- type : bool
- output user list

**Parameter --passwordfile, -p**
- type : bool
- output password list

<br/>
<br/>

**Example 1**

`py breach-parse.py @yahoo.com yahoo`

- Search data with `@yahoo.com`
- Outputs `yahoo.txt`


**Example 2**

`py breach-parse.py @yahoo.com yahoo --userfile`

- Search data with `@yahoo.com`
- Outputs `yahoo.txt`
- Outputs `yahoo_users.txt`

**Example 3**

`py breach-parse.py @yahoo.com yahoo --passwordfile`

- Search data with `@yahoo.com`
- Outputs `yahoo.txt`
- Outputs `yahoo_users.txt`
- Outputs `yahoo_password.txt`

**Example 4**

`py breach-parse.py @yahoo,com yahoo -u -p`

- Search data with `@yahoo.com`
- Outputs `yahoo.txt`
- Outputs `yahoo_users.txt`
- Outputs `yahoo_password.txt`
