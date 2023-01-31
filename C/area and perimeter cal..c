#include<stdio.h>
int main()
{
	//Declaring the integers
	const float pi=3.14;
	float Length=0,Breadth=0,radius=0;
	float AreaR=0,AreaC=0,PerimeterR=0,PerimeterC=0;
	//Taking input form the user
	printf("Enter the Length ");
	scanf("%f",&Length);
	printf("Enter the Breadth");
	scanf("%f",&Breadth);
	printf("Enter the radius");
	scanf("%f",&radius);
	//Calculations
	AreaR=Length*Breadth;
	AreaC=pi*radius*radius;
	PerimeterR=2*(Length+Breadth);
	PerimeterC=2*pi*radius;
	//results
	printf("----------------------------------\n");
	printf("The resutls are :- \nArea of rectangle=%f\nArea of circle=%f\nPerimeter of rectangle=%f\nPerimeter of circle=%f\n",AreaR,AreaC,PerimeterR,PerimeterC);
	return 0;
}
