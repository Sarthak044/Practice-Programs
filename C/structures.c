#include<stdio.h>
struct student
{
	int rollno;
	char name[50];
};
 void main()
{
	struct student stu1,stu2;
	printf("Enter your name student 1: ");
	scanf("%s",stu1.name);
	printf("\nEnter you roll no. : ");
	scanf("%d",&stu1.rollno);
	printf(" \nYour name is : %s\n",stu1.name);
	printf("Your rollno. is : %d ",stu1.rollno);
}
