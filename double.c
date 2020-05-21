#include<stdlib.h>
#include<stdio.h>
int main(void)
{
	void *chunk1,*chunk2,*chunk3;
	chunk1 = malloc(0x10);
	chunk2 = malloc(0x10);
	free(chunk1);
	free(chunk2);
	free(chunk3);
	printf("%s","Hello world");
	return 0;
}
