#include<stdio.h>
main()
{
	float cel,far;
	printf("Enter the Temperature in degree celsius\n");
	scanf("%f",&cel);
	printf("The temperature in degree fahrenheit is\n");
	far=(cel*9/5)+32;
	printf("%f",far);
	return 0;
	
}
