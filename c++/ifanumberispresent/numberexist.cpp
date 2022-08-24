#include<iostream>
using namespace std;

int main(){
    int size, arr[size],i, num;
    cout<<"Enter the number to find"<<endl;
    cin>>num;
    cout<<"Enter the size of the array"<<endl;
    cin>>size;
    //input
    for(i=0;i< size; i++){
        cin>>arr[i];
    }

    // to find if the given number is present or not with first index
    // if not print -1

    for(i=0;i<size;i++){
        if (arr[i] == num){
            cout<<arr[i]<<" is Present"<<endl;  
            cout<<"Index is "<< i <<endl;
            return 0;      
        }
    }
    cout<<"-1"<<endl;
}