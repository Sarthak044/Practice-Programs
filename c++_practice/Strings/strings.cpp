#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int main(){
    // char arr[4] = {'a','b','c','d'};

    // for (int i=0;i<4;i++){
    //     cout<<arr[i]<<" ";
    // }
    // '\0' --> NULL char

    //strings

    string s = "";
    // If you have to print the whole line
    
    getline(cin , s);
   // cout<<s<<endl;

    for(int i=0;s[i]!='\0';i++){
        cout<<s[i];
    }
    cout<<endl;
  
    //for size of the string 
    cout<<s.size()<<endl;
    
    //sort and reverse
    sort(s.begin(), s.end());
    reverse(s.begin(), s.end());
    
}