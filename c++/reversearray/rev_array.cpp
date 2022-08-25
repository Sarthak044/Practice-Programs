#include<iostream>
#include<algorithm>
using namespace std;

int main(){

    int size;
    cin>>size;
    int arr[size],i;
    
    for (i=0;i<size;i++){
        cin>>arr[i];
    }

    //Reverse an array shortcut with sort and reverse function

    reverse(arr, arr+size);
    for(i=0;i<size;i++){
        cout<<arr[i]<<" "<<endl;
    }

    // for finding the kth min and max number
    int k;
    cout<<"Enter the Kth element"<<endl;
    cin>>k;
    sort(arr, arr+size);
    cout<<"Kth min = "<<arr[k-1]<<endl;
    cout<<"Kth max = "<<arr[size-k]<<endl;

    }