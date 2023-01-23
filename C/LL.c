#include<stdio.h>
#include<conio.h>

int main()
{
    int a[100],i,n,search;
        printf("Enter the no. of elements to insert");
        scanf("%d",&n);
        printf("enter the no");
        scanf("%d",&search);
            for(i=0;i<n;i++)
            {
                if(a[i]==search)
                {
                    printf("element is at %d",i+1);
                    break;
                }
                if(i=n+1)
                {
                    printf("element not found");
                }
            }
            getch();
}
