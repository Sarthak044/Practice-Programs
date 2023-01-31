#include<stdio.h>
#include<string.h>
int main()
{
	char str1[20],str2[10];
	puts("Enter the two strings : \n");
	gets(str1);
	gets(str2);
	strcnp(str1, str2);
	puts(str1);
	return 0;
	
	
	
}
