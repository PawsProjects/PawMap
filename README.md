# PawMap
Simple Web API for Zmap/Masscan

## Pre-Request
- Python 3.6+
- Zmap
- Masscan
- Sanic(Python)

## Config
- Clone this repo
- Install Requirements.txt
- Change ALL PASSWORD in main.py with `{{HERE}}`
- Configure the bind ip and port in __MAIN__
- Run`python main.py`


## Usage
- Configure IP blacklist
  - `GET` /webzmap/web/setblacklist.sh
    - Parameter: `key, ip`
    - Description: 
      - Key: Password
      - ip: ip list of the blacklist
    - Usage:
      - Used to Add Blacklist
  - Example:
    - `GET` /webzmap/web/setblacklist.sh?key={{HERE}}&ip=127.0.0.1
  ------
  - `GET` /webzmap/web/getblacklist.sh
    - Parameter: `key`
    - Description: 
      - Key: Password
    - Usage:
      - Used to Get Blacklist
    - Example:
      - `GET` /webzmap/web/getblacklist.sh?key={{HERE}}

- Use Zmap to Scan
  - `GET` /webzmap/web/zmap.sh
    - Parameter: `ips, port, maxs`
    - Description: 
      - ips: ip list
      - port: port
      - maxs: max Result Number [0, 100000]
    - Usage:
    - Example:
      - `GET` /webzmap/web/zmap.sh?ips=192.168.0.1/25&port=80&maxs=100

- Use Masscan to Scan
  - `GET` /webzmap/web/masscan.sh
    - Parameter: `ips, port, time`
    - Description: 
      - ips: ip list
      - port: port
      - time: timeout [0, 120]s
    - Usage:
    - Example:
      - `GET` /webzmap/web/masscan.sh?ips=192.168.0.1/25&port=80&time=10

- Get Exists Scan Result
  - `GET` /webzmap/web/getresult.sh
    - Parameter: `key, port`
    - Description: 
      - key: Password
      - port: Which port you want to get
    - Usage:
    - Example:
      - `GET` /webzmap/web/getresult.sh?key={{HERE}}&port=80

## Disclaimer
- What you can do
  - Follow the disclaimer of Zmap/Masscan
  - Use  to scan your own network
  - Use to scan the network you have permission to scan
- We have no responsibility for any illegal use of this tool
- Please follow the local lows when you used this program.