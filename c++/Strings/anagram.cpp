#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

string anagram_check(string s1, string s2){
    sort(s1.begin(), s1.end());
    sort(s2.begin(), s2.end());

    if(s1 == s2){
        return "Yes";
        
    }
    else{
        return "No";
    }
}
int main(){

string s1,s2;
cin>>s1>>s2;
string check = anagram_check(s1,s2);
cout<<check<<endl;
}