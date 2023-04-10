#!/bin/python3

from morimod import search
BRAND = "Tyan"
MB = "B7105F48TV4HR-2T-N"

#print(search.BIOS(BRAND,MB))
#print(search.BMC(BRAND,MB))
print("a[contains(@href,'{}')]".format(BRAND.lower()))
print(search.search_google(BRAND,MB))
