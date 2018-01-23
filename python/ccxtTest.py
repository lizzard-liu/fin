#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import flexx


import ccxt 
config={
"apiKey": "fb747aac-fea3dc92-d6883b44-0cd0c",
"secret": "774f497b-605bc525-10eb49ed-310d4"
}
hb = ccxt.huobipro(config)
pair='BTC/USDT'

print("id: "+ hb.id + " name: " + hb.name)


print("------ load_markets:")
for item in hb.load_markets():
    #print item
    pass

print("------ markets keys:")
print(list(hb.markets.keys()))
for item in list(hb.markets.keys()):
    print(item)
    #pass


print("------ symbols:")
for item in hb.symbols:
    #print(item)
    pass

print("------ currencys:")
for item in hb.currencies:
    #print(item)
    pass


print("------ market:")
print(hb.markets[pair])
for item in hb.markets[pair]:
    print(item)
    #pass


print("------ market:")
for item in hb.market(pair):
    #print item
    pass


print("------ market by id ")
print(hb.markets_by_id['btcusdt']['id'])

	

print("------ methods")
for item in dir(hb):
    print(item)


print("------ balance:")
for item in hb.fetchBalance():
    print(item)
print(hb.fetchBalance())
