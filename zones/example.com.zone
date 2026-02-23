; =====================================================================
; Example DNS zone file template
;
; This file is provided as a **template**. Users should modify the
; domain names, IP addresses, and other records according to their
; own needs.
;
; Based on the official references:
;   - NSD:  https://nsd.docs.nlnetlabs.nl/en/latest/zonefile.html
;   - BIND9: https://bind9.readthedocs.io/en/latest/chapter3.html
;
; Other resources:
;   - Zone Files: https://en.wikipedia.org/wiki/Zone_file
;   - RRs: https://en.wikipedia.org/wiki/List_of_DNS_record_types
; =====================================================================

$ORIGIN example.com.
$TTL 86400 ; Zone default TTL

; In the SOA (Start of Authority) record, the first domain specifies 
; the main authoritative name server for the zone. The second domain 
; represents the administrator's email for this zone, where the first 
; dot (.) is replaced by an @ sign. For example, in the above SOA, 
; the email would be: noc@dns.example.org. If the local part of the 
; email contains dots, they should be escaped with a backslash (\).

; The @ symbol can be used as a shorthand for the zone's origin domain. 
; For instance, instead of writing example.com. IN SOA, you can simply 
; write @ IN SOA. The same applies to other records like A or MX: 
; @ A 192.0.2.1 is equivalent to example.com. A 192.0.2.1.

@   IN      SOA     ns1.example.com. noc.example.com. (
        2026080801 ; serial number
        12h        ; refresh
        15m        ; update retry
        4d         ; expiry
        2h         ; minimum
)

; In DNS zone files, the class of a record (usually IN for Internet) 
; can be omitted after it has been set once. When omitted, the class 
; of the previous record is automatically applied. 
; 
; For example, in the SOA record above we set the class to IN. All 
; following NS, A, and MX records inherit this class implicitly, 
; so it's not necessary to repeat IN every time. 
; Writing IN explicitly is optional but can improve clarity.

; name server RR for the domain
@            IN      NS      ns1.example.com.

; the second name server is external to this zone (domain)
@            IN      NS      ns2.example.net.

; mail server RRs for the zone (domain)
@        3w  IN      MX  10  mail.example.com.

; the second  mail servers is  external to the zone (domain)
@            IN      MX  20  mail.example.net.

; domain hosts includes NS and MX records defined above
; plus any others required
; for instance a user query for the A RR of joe.example.com will
; return the IPv4 address 192.168.254.6 from this zone file.
; Each host in the zone can have one or more IPv4 addresses defined
; using the A record. Example:

ns1         IN      A       192.168.254.2
mail        IN      A       192.168.254.4
joe         IN      A       192.168.254.6
www         IN      A       192.168.254.7

; To support IPv6, define AAAA records with the host's IPv6 address.
; Syntax is the same as A records, just use AAAA instead.

ns1         IN      AAAA    2001:db8:1::2
mail        IN      AAAA    2001:db8:1::4
joe         IN      AAAA    2001:db8:1::6
www         IN      AAAA    2001:db8:1::7

; aliases ftp (ftp server) to an external domain
ftp         IN      CNAME   ftp.example.net.
