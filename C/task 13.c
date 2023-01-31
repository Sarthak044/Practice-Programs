#include<stdio.h>
 
int main()
{
	int n[10],i=0,a,max,min;
	printf("How many elements\n");
	scanf("%d",&a);
	printf("Enter the Array\n");
 
	for(i=0;i<a;++i)
		scanf("%d",&n[i]);
	
	max=min=n[0];
	for(i=1;i<a;++i)
	{
		if(n[i]>max)
			max=n[i];
		if(n[i]<min)
			min=n[i];
	}
	
	printf("The largest element is %d",max);
	printf("\nThe smallest element is %d",min);
 
	return 0;
}
