#include<stdio.h>
main()

/*
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* * 
*
*/
// Following pattern will be made//
{
	int i=0,j=0;

	for(i=1;i<=5;i++)
	{
		for(j=1;j<=i;j++)
		{
			printf("*\t"); 
}
		   printf("\n");
	}
	for(i=4;i>0; i--)
	{
		for(j=0;j<i;j++)
		{
	
	printf("*\t");
}

    printf("\n");
}
	
	
	return 0;
		
	}
