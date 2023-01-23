#include<stdio.h>
#include<string.h>
main()
{
	int n,k,d,result=0;
	printf("Enter the no. you want to check\n");
	scanf("%d",&n);
	k=n;
	while(n>0)
	{
		d=n%10;
		n=n/10;
		result =result +(d*d*d);
		
	}
	if(k=result)
	printf("%d is the armstorng no.",k);
	else 
	printf("The given no. is not armstrong");
		
}


