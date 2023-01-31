#include<stdio.h>
int main()

{
	/*
	1
	12
	123
	1234
	12345
	*/
	//following pattern will be printed//
	int i,j;
	for(i=1;i<=5;i++)
	{
		for(j=1;j<=i;j++)
		printf("%d",j);
		printf("\n");
	}
}
