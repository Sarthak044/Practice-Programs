#include<stdio.h>
main()
{
	int S1[3][3],S2[3][3],C;
	int i=0,j=0;
	printf("Enter the 1st matrix\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		scanf("%d",&S1[i][j]);
	}
	printf("Enter the second matix\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		scanf("%d",&S2[i][j]);
	}
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		if(i==j)
		C=S1[i][j]+S2[i][j];
		printf("the sum of the matrix is %d",C);
		
	}
}
