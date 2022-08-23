#include<iostream>
using namespace std;

int main(){
    cout<<"reversing a number"<<endl; 

    int num;
    int ld,rev=0;
    cin>>num;
    int orginal = num;
    while(num !=0 ){
        ld = num%10;
        rev = (rev*10) + ld;
        num = num/10;
    }
    cout<<rev<<endl;
    if (orginal == rev){
        cout<<"Palindrome"<<endl;
    }
    else{
        cout<<"Not Palindrome"<<endl;
    }
}
