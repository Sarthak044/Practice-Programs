#include<bits/stdc++.h>
using namespace std;

int main(){
    // to remove vowles from the given string

    string s = "sarthak kulshrestha";
    string consonants =  ""; 
    string vowels = "";
    for(int i=0;i<s.size();i++){
        if(!(s[i] == 'a' || s[i] == 'e' ||s[i] == 'i' ||s[i] == 'o' ||s[i] == 'u')){
            consonants +=s[i];
        }
        else{
            vowels +=s[i];
        }
    }
    cout<<consonants<<endl;
    cout<<vowels<<endl;
}