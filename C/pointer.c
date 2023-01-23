#include<stdio.h>
main()
{
	int a=20;
	int *p=&a;
	a=*p;
	printf("the address of the following data of %d is : %d",a,p);
}
