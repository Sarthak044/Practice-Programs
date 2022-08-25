#include<iostream>
using namespace std;

int main(){
    //Rotate the array by 1 position on the right 
    // suppose an array [3,2,1,0]
    // [0,3,2,1]

    int size;
    cin>>size;
    int arr[size], i;
    
    for(i=0;i<size;i++){
        cin>>arr[i];
    }
    
    int last = arr[size-1];
    for (i=size-1;i > 0;i--){
        arr[i] = arr[i-1];
        
    }
    arr[0] = last;
    for (i=0;i<size;i++){
        cout<<arr[i]<<" ";
    }
}