# dns-spray-domain-controllers
Fetch Domain Controllers via DNS SRV entries and send them DNS queries


This module is a simply hack to check if Domain Controllers are logging. It performs lookups of SRV records against a domain. In Microsoft AD  environments, this will return the Domain Controllers. Once the Domain  Controllers are fetched, a DNS lookup for a specific domain will be sent  to these. If DNS logging and log forwarding is enabled on the DCs, the  domain should show up in the SIEM logs.
