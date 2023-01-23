#include<stdio.h>
#include<string.h>
#include<conio.h>
main()
{
	char name[10];
	int phn, age;
	//input program//
	puts("enter the name of the applicant");
	gets(name);
	printf("Enter the phone no. of the applicant\n");
	scanf("%d",&phn);
	printf("Enter the age of the applicant\n");
	scanf("%d",&age);
	printf("************************************************\n");
	//output program//
	printf("Name of the applicant is ");
	puts(name);
	printf("The age of the applicant is %d\nThe phone number of the applicant is %d\n",age,phn);
	return 0;
	
	
}
