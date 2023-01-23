#include<stdio.h>
//To collect Recipt no,Description,Date// 
struct bill 
{
	int rno;
	char date[13];
	char desc[30];
};
main()
{
	int choice;
	struct bill b1;
printf("Choose from the following options \n1. Make a bill\n2. Quit");
scanf("%d",&choice);
switch(choice)
{
case 1: 
printf("Enter your bill no.");
scanf("%d",&b1.rno);
printf("\nEnter the date of the bill");
scanf("%s",&b1.date);
printf("Enter the description");
scanf("%s",&b1.desc);
printf("**********************************************\n");
printf("your Bill is  \n1. Recipt no. %d\n2. Date of the bill %s\n3. Description of the bill %s\n",b1.rno,b1.date,b1.desc);
break;
case 2:
	printf("Have a nice day");
	break;

default:
	printf("Invalid Input");
}
	return 0;
	}
