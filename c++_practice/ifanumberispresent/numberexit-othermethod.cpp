#include<iostream>
using namespace std;

int main(){
    int size,i, num;
    cout<<"Enter the size of the array"<<endl;
    cin>>size;
    int arr[size];
    cout<<"Enter the number to find"<<endl;
    cin>>num;
    
    //input
    for(i=0;i< size; i++){
        cin>>arr[i];
    }

    // to find if the given number is present or not with Last index
    // if not print -1
    int index = -1;
    for(i=0;i<size;i++){
        if (arr[i] == num){
            index = i;
        }
    }
    cout<<index<<endl;
//     cout<<"-1"<<endl;
}