from ping3 import ping, verbose_ping

ipadrr = input("Please enter the IP Adrress: ")
dmin = input("If possible, please enter the Domain Address: ")

# Checks for Ping and see's if pinging is possible 
def pingfunc(rslt_nodmin, rslt_dmin):
    if not dmin:
        rslt_nodmin = verbose_ping(ipadrr, timeout=2)
        if rslt_nodmin is False:
            print("Invalid IP Address: {ipaddrr}, can not be pinged or is invalid")
            return
    else:
        rslt_dmin = verbose_ping(dmin, timeout=2, src_addr={ipadrr})
        if rslt_dmin is False:
            print("Invalid IP Address: {ipaddrr} & {dmin}, can not be pinged or is invalid")

pngf = pingfunc(ipadrr, dmin)
if dmin:
    print(f'${rslt_dmin}')
else:
    print(f'{rslt_nodmin}')