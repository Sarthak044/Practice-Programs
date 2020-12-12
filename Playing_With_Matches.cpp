#include<iostream>
using namespace std;

int main()
{
    int T;
    cin>>T;
    while(T>0)
    {
    int i=0,sticks[10]={6,2,5,5,4,5,6,3,7,6};
    long long int A=0,B=0,sum=0,r=0,n=0;
    cin>>A>>B;
    sum=A+B;
    while(sum!=0)
    {
        r=sum%10;
        
        for(i=0;i<10;i++)
    {
        if (r==i)
        {
            n+=sticks[i];
            break;
        }
        
    }
    sum=sum/10;
    }
    cout<<n<<endl;

    T--;
    }
return 0;

}
