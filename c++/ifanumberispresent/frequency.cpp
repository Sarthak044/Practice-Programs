#include<iostream>
using namespace std;

int main(){
    int size;
    cin>>size;
    int arr[size],i;
    for (i=0;i<size;i++){
        cin>>arr[i];
    }
    // to find the frequency of the given number in an array
    int num;
    cin>>num;
    int temp = 0;
    for (i=0;i<size;i++){
        if (arr[i] == num){
            temp ++;
        }
    
    }
    cout<<temp<<endl;
}