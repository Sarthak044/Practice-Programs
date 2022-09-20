#include<iostream>
using namespace std;

int main(){

    int n;
    int arr[n];
    int i;
    cin>>n;
    for (i=0;i<n;i++){
        cin>>arr[i];
    }

    // to find smallest number in an given array
    int minnum = arr[0];
    for (i=0; i<n ;i++){
        if (arr[i] < minnum){
            minnum = arr[i];
        }
    }
    cout<<minnum<<endl;

}