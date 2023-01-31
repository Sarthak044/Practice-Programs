#include<stdio.h>
void main()
{
	char temp;
	int cel,far;
	printf("Choose from the following\n1. CELCIUS to FAHRENHEIT\n2.FAHRENHEIT to CELCIUS\n3.EXIT\n");
	scanf("%d",&temp);
	switch(temp)
	{
		case 1:
			printf("Enter the temperature in Celcius\n");
			scanf("%d",&cel);
			far=(cel*9/5)+32;
			printf("Temperature in Fahrenheit is %d",far);
			break;
		case 2:
			printf("Enter the temperature in Fahrenheit\n");
			scanf("%d",&far);
			cel= (far-32)*5/9;
			printf("Temperature in Celcuis is %d",cel);
			break;
		case 3:
			printf("Thanks for your time");
			exit(0);
			break;
		default:
			printf("INVALID OPERATION/n PLEASE TRY AGAIN ");
			
				
	}
	
}

