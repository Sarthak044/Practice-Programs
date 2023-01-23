#include<stdio.h>
#include<string.h>
#include<stdlib.h>
main()
{
	int tuna=19;
	printf("memory address of the variable  is %p\n",&tuna);
	printf("name of var. is tuna\n");
	printf("the value of var is %d\n",tuna);
	
	int *ptuna=&tuna;
	printf("the address of the var is %p",ptuna);
}
