from pwn import *
# nc week-1.hgame.lwsec.cn 32069
ip = "week-1.hgame.lwsec.cn"
port = "32069"
r = remote(ip,port)
r.interactive()
