#include<stdio.h>
#include<string.h>
//void output();//
struct Store{
	char author[20];
	char title[20];
	char genre[20];
}a;
void output()
{
	printf("The authors name is %s\n",a.author);
	printf("The title of the book is %s\n",a.title);
	printf("The genre of the book is %s\n",a.genre);
	
}
main()
{
	printf("Enter the Authors name\n");
	gets(a.author);
	printf("Enter the title of the book\n");
	gets(a.title);
	printf("Enter the genre of the book\n");
	gets(a.genre);
	printf("----------------------------------------------------\n");
	output();
}
