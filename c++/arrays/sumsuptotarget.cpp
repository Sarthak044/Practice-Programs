#include<iostream>
using namespace std;

int main(){
    /*Question --
    Given an array and an integer target. Print yes if there is a pair in the 
    array that sums up to the target
    */

   int size;
   cin>>size;
   int arr[size];
   
   //INPUT
   for(int i=0;i<size;i++){
       cin>>arr[i];
   }

   int target;
   cin>>target;

   for (int i=0;i<size;i++){
       for (int j=i+1;j<size;j++){
           if (arr[i]+ arr[j]==target){
               cout<<"Yes "<<arr[i]<<" and "<<arr[j]<<endl;
               return 0;
           }
       }
   }
   cout<<"No"<<endl;
}