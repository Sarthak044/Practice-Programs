#include<bits/stdc++.h>
using namespace std;

int main(){
    int n,i;
    cin>>n;
    int arr[n];
    for(i=0; i<n; i++){
        cin>>arr[i];
    }
    // MAX CODE
    int mx = arr[0];
    int s_mx = INT_MIN;
    for (i=0; i<n;i++){
        if (arr[i]>mx){
            mx = arr[i];
        }
    }
    for(i=0;i<n;i++){
        if(arr[i] != mx){
            if(arr[i] > s_mx ){
                s_mx = arr[i];
            }
        }
    }
    cout<<"Second Max is: "<<s_mx<<endl;

    //MIN CODE
    int min = arr[0];
    int s_min = INT_MAX;
    for(i=0;i<n;i++){
        if (arr[i]<min){
            min = arr[i];
        }
    }

    for(i=0;i<n;i++){
        if(arr[i] != min){
            if(arr[i]<s_min){
                s_min = arr[i];
            }
        }
    }
    
    cout<<"Second Min is: "<<s_min<<endl;
    
}