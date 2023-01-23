#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define size 30
struct ele{
int b[size];
int c;	
};
struct student{
	int roll no;
	char name[10];
	int cl;
	};
	
typedef struct student DATA2;
typedef struct ele DATA;
void add();
void sub();
void display();
void main()
{
	int a,d=1;
	DATA.c= -1;
	printf("Choose a option");
	while(d)
	{
	
	printf("*******************************************************************\n");
	printf("1.Enter the data of the student\n2.Remove the data of the student\n3.Display the data\n4.EXIT\n");
	printf("*******************************************************************\n");
	scanf("%d",&a);
	switch(a)
	{
		case 1:
		{
			Printf("Enter the data");
			add();
			break;
		}
		case 2:
			{
			sub();
			break;
			}
		case 3:
		{
			display();
			break;
			}
		case 4: return;	
	}
	fflush(stdin);
	printf("Do you want to continue(Type 1 for yes or 0 for no)?\n");
	scanf("%d",&d);
}
}
	void add()
	
	{
		int n;
		if(ele.b==(size-1))
	{
		printf("No more students can be added\n");
		return;
	}
		else 
		{
		 printf("Enter the Name of the student\n");
	scanf("%s",&DATA2.name[10]);
	printf("Enter the Roll no. of the student\n");
	scanf("%d",&DATA2.roll no);
	printf("Enter the class of the student\n");
	scanf("%d",&DATA2.cl);
	DATA.c= DATA.c+1;
	DATA.b[DATA.c]=n;
	
	}
	return;
	}
	void sub()
	{
		
	}
	
