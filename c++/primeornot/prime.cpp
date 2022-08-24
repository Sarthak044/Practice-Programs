#include<iostream>
using namespace std;

bool primrOrNot(int num){
    int i;
    if (num == 1){
        return false;
    }
    for (i=2;i<=num-1;i++){
        if (num%i == 0){
           return false;
        }
    }
    return true;
}

int main(){
    //print all numbers between a and b
    int a,b;
    cin>>a>>b;
    for (int i=a;i<=b;i++){
        if (primrOrNot(i)){
            cout<<i<<endl;
        }
    }
}