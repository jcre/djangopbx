#!/bin/bash
/usr/bin/sudo /usr/sbin/nft delete element netdev filter ipv6_block_list { $1 }
