# breach-parse.py

## Synposis
The same [breach-parse](https://github.com/hmaverickadams/breach-parse) tool from [hmaverickadams](https://github.com/hmaverickadams) but written in python3. Only works on Linux.. sorry Windows users. 

## Description
This tool runs about a minute faster than it's bash counterpart and is more accurate when searching. 

The bash version uses `grep -a -E "$1" "$file"` for searches. The `-E` enables extended regex comparision, therefore if your search term is `@bob.com` you can potentially get false positives such as `@bobscom.com`. This tool uses python's `in` keyword for an exact string comparision. 

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
