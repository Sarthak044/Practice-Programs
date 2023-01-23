#include<stdio.h>
#include<string.h>
main()
{
	char name1[10];
	char name2[10];
	printf("Enter the first name\n");
	gets(name1);
	printf("Enter the second name\n");
	gets(name2);
	strcat(strcat(name1, " "),name2);
	printf("%s",name1);
	
}
