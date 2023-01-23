#include<stdio.h>
main()
{
	//MARKS INPUT PROG//
	int math,sci,eng,sum=0;
	float avg=0;
	printf("Enter the marks of math\n");
	scanf("%d",&math);
	printf("Enter the marks of science\n");
	scanf("%d",&sci);
	printf("Enter the marks of english\n");
	scanf("%d",&eng);
	//SUM AND AVERAGE PROG//
	sum= math+sci+eng;
printf("The sum is %d\n",sum);
avg=sum/3;
printf("The average marks are %f/n",avg);
return 0;
}
