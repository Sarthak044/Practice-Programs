#include<stdio.h>
#include<conio.h>
#define SIZE 5
struct stack
{
	int stk[SIZE];
	int top;
};
typedef struct stack Stack;
STACK s;
// Function declaration//prototype//
void push(void);
int pop(void);
void display(void);
 void main()
 {
 	int choice
 	int option=1

 	s.top=-1
 	printf("Stack Operation\n");
 	while(option)
 	{

 		printf("***************************************");
 		printf("1.Push\n2.Pop\n3.Display\n4.Exit");
 		Printf("Enter your choice");
 		scanf("%d",&choice);
 		switch(choice)
 		{
 			case 1: push();
 			break;
 			case 2: pop();
 			break;
 			case 3: Dispaly();
 			break;
 			case 4:Exit();
 			break;

		 }
		 fflush(stdin);
		 printf("Do you want to continue\n Type 1 for yes, 0 for no\n");
		 scanf("%d",&option);

	}
 }
 void push ()
 {
 	int num;
 	if(s.top == (SIZE-1))
 	{
 		printf("Stack is full\n");
	 }
	 else
	 {
	 	printf("Enter the element to be pushed\n");
	 	scanf("%d",&num);
	 	s.top=s.top+!;
	 	s.stk[s.top]=num;

	 }
	 return;
}
void pop ()
int

 }
