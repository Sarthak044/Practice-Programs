#include<stdio.h>
main()
{
	int a,r,rev=0;
	printf("Enter a no. to reverse\n");
	scanf("%d",&a);
	while(a>0)
	{
		r=a%10;
		rev=rev*10+r;
		a=a/10;
		
	}
	printf("%d",rev);
	return 0;
}
