# breach-parse

## Synposis
The same [breach-parse](https://github.com/hmaverickadams/breach-parse) tool from [hmaverickadams](https://github.com/hmaverickadams) but written in python3. Only works on Linux.. sorry Windows users. 

## Description
This tool runs about a minute faster than it's bash counterpart and is more accurate when searching. 

The bash version uses `grep -a -E "$1" "$file"` for searches. The `-E` enables extended regex comparision, therefore if your search term is `@bob.com` you can potentially get false positives such as `@bobscom.com`.

## Usage

**Parameter -ip**
- type : str
- one or more ips in csv format

**Example 1**


`py find-messageTypeAnomalies.py -c  "134248483" -v`

- Uses the alias of parameter --cid to specify the customer id number
- Uses verbose output
