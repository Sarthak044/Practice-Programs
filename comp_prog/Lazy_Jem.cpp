#include<iostream>
using namespace std;
int main()
{
    int T;
    cin>>T;
    while(T>0)
    {   
        long long int n=0,b=0,m=0,t=0;
        cin>>n>>b>>m;
           
        while(n>0)
        {
            long long int mid=0;
            if(n%2==0)
            {
                mid=n/2;
            }
            else if(n%2!=0)
            {   
                mid = (n+1)/2;
            }
            t=t+(mid*m)+b;
            m=m*2;
            n=n-mid;
        }
        cout<<t-b;
        cout<<endl;
        T--;
    }

    return 0;
}
