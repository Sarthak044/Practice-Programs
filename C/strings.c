#include<stdio.h>
#include<string.h>
main()
{
	char num[30];
	char a;
	int j=0,i=0;
	puts("Enter a data : \n");
	gets(num);
	printf("Enter a word to be searched : ");
	scanf("%c",&a);
	for(i=0;num[i]!='\0';i++)
	{
		if(a==num[i])
		j++;
	}
	printf("The frequency of %c is : %d \n",a,j);
	return 0;
	
}
