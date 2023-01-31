#include<stdio.h>
int main()
{
	//Declaring the variables//
	int i,j,rows;
	//Taking input from the user//
	printf("no. of rows you want\n");
	scanf("%d",&rows);
	
	for(i=1;i<=rows;i++)
	{
		for(j=1;j<=rows;j++)
		{
		
		if(i==1||i==rows||j==1||j==rows)
		{
		printf("*\t");
	}
	else
	{
		printf(" \t");
		
	}
}
printf("\n");
}
return 0;
	
	
}
