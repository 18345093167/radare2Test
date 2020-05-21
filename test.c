//gcc test.c -o test -m32
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int test(int a,int b){
	//int len = 0;
	//len = strlen(a);
	return a+b;
}
int main()
{
      	printf("hello world");
 	char a[100];
	scanf("%s",a);
	printf(a);
	int len = test(1,2);
	printf("%d\n",len);
        return 0;
}

