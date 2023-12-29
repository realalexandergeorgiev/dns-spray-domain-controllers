# dns-spray-domain-controllers
Fetch Domain Controllers via DNS SRV entries and send them DNS queries


This module is a simply hack to check if Domain Controllers are logging. It performs lookups of SRV records against a domain. In Microsoft AD  environments, this will return the Domain Controllers. Once the Domain  Controllers are fetched, a DNS lookup for a specific domain will be sent  to these. If DNS logging and log forwarding is enabled on the DCs, the  domain should show up in the SIEM logs.
## Example Output

```
#########################################################
 Using AD domain btc.bw and trigger query fooo.daloo.de
#########################################################
[ ] Fetching SRV records for _ldap._tcp.dc._msdcs.btc.bw
[+] Found SRV record bwgahqaddc01.corp.btc.bw
[+] Found SRV record bwgahqaddc03.corp.btc.bw
[+] Found SRV record bwgahqaddc02.corp.btc.bw
[+] Found SRV record bwgahqaddc04.corp.btc.bw
[ ] Sending DNS query (fooo.daloo.de) to DC bwgahqaddc01.corp.btc.bw
[+] bwgahqaddc01.corp.btc.bw resolved fooo.daloo.de to 5.45.103.155
[ ] Sending DNS query (fooo.daloo.de) to DC bwgahqaddc03.corp.btc.bw
[+] bwgahqaddc03.corp.btc.bw resolved fooo.daloo.de to 5.45.103.155
[ ] Sending DNS query (fooo.daloo.de) to DC bwgahqaddc02.corp.btc.bw
[+] bwgahqaddc02.corp.btc.bw resolved fooo.daloo.de to 5.45.103.155
[ ] Sending DNS query (fooo.daloo.de) to DC bwgahqaddc04.corp.btc.bw
[+] bwgahqaddc04.corp.btc.bw resolved fooo.daloo.de to 5.45.103.155
```
