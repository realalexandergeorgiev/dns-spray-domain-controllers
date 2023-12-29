#!/usr/bin/env python3
"""
Description: 
This module is a simply hack to check if Domain Controllers are logging.
It performs lookups of SRV records against a domain. In Microsoft AD 
environments, this will return the Domain Controllers. Once the Domain 
Controllers are fetched, a DNS lookup for a specific domain will be sent 
to these. If DNS logging and log forwarding is enabled on the DCs, the 
domain should show up in the SIEM logs.

Author: Alexander Georgiev
Date: 2023-12-29
"""
import dns.resolver

domain_to_query="invalidfooo.daloo.de"
ad_domain="btc.bw"

def get_domain_controllers(domain):
  domain_controllers = []
  try:
    print(f"[ ] Fetching SRV records for _ldap._tcp.dc._msdcs.{domain}")
    srv_records = dns.resolver.resolve("_ldap._tcp.dc._msdcs." + domain, 'SRV')
    for srv in srv_records:
      res = str(srv.target).rstrip('.')
      domain_controllers.append(res)
      print(f"[+] Found SRV record {res}")
  except Exception as e:
    print("[-] Failed with exception:",e)
  return domain_controllers

def lookup_domain(domain):
  domain_controllers = get_domain_controllers(ad_domain)
  for dc in domain_controllers:
    print(f"[ ] Sending DNS query ({domain_to_query}) to DC {dc}")
    try:
      answers = dns.resolver.resolve(domain, 'A', raise_on_no_answer=False)
      if answers:
        for answer in answers:
          print(f"[+] {dc} resolved {domain} to {answer}")
      else:
        print(f"[-] {dc} could not resolve {domain}")
    except dns.resolver.NXDOMAIN:
      print(f"[-] Could not find SRV record for {domain} (NXDOMAIN)")
    except dns.resolver.NoAnswer:
      print(f"[-] Could not find SRV record for {domain} (NoAnswer)")
    except dns.resolver.NoNameservers:
      print(f"[-] Could not find SRV record for {domain} (No NS)")
    except Exception as e:
      print("[-] Failed with exception:",e)

print(f"#########################################################")
print(f" Using AD domain {ad_domain} and trigger query {domain_to_query}")
print(f"#########################################################")
lookup_domain(domain_to_query)
