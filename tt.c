#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void win()
{
system("/bin/sh");
}
void main(int argc, char *argv[])
{
char buf[103];
fgets(buf, 103, stdin);
buf[strlen(buf)-1] = 0x0;
printf(buf);
exit(0);
}