from pwn import *

host = "forever.isss.io"
port = 9018

p = remote(host, port)


for _ in range(0, 35):
    response = p.recvuntil("What will you do next?")
    print(response.decode())
    p.sendline("1")

p.sendline("2")
p.interactive()
