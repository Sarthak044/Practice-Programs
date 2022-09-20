#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    int arr[n];
    
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    //Max
    int mx = arr[0];

    for(int i=0;i<n;i++){
        if (arr[i]>mx){
            mx = arr[i];
        }
    }
    cout<<mx<<endl;

    //2nd Max
    int mx2 = INT_MIN;
    for(int i=0;i<n;i++){
        if (arr[i] != mx && arr[i]>mx2){
            mx2 = arr[i];
        }
    }
    cout<<mx2<<endl;
    
}
