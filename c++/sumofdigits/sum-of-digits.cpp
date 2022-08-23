#include<iostream>
using namespace std;

int sumOfDigits(int num){
    int sum=0;
    int ld;
    while(num != 0){
        ld = num%10;
        sum += ld;
        num /=10;
    }
    return sum;
}

int main(){
    int num;
    cin>>num;
    int sod = sumOfDigits(num);
    cout<<sod<<endl;
}