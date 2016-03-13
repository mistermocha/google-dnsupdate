# google dnsupdater script

This script is meant to run in a cron. It will consume /etc/googledomains.ini for configs (domain, username, password) for instructions on how to access your google domains api ([as documented here](https://support.google.com/domains/answer/6147083?hl=en&_ga=1.213322900.1880335840.1439780633)).

Configure your ini config like this:

```ini
[DEFAULT]
# Should just return an IPv4 addr
ipsource = http://canihazip.com/s

[my.domain.tld]
username = sekretusername
password = sekretpasswerd
```

Note that [canihazip.com/s](http://canihazip.com/s) returns just an IP address with no stylization. This is perfect for API calls like this. If they happen to fall over at any time, we will just have to figure out a new source of truth for IP addressing.

More to come to make this better. Patches and fixes welcome!
