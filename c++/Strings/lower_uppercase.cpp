// #include<iostream>
// #include<string>
// #include<algorithm>
// #include<cctype>
#include<bits/stdc++.h>

using namespace std;

int main(){
    // lower to upper case
    string a = "sarthak";
    if (a[0]>= 'a' && a[0]<='z'){

    a[0] -= 32; //ASCII reference 
    cout<<a<<endl;

    }
    else{
        cout<<a<<endl;
    }

    //upper to lower
    string b = "Sarthak";
    if (a[0]>= 'A' && a[0]<='Z'){

    a[0] += 32; //ASCII reference 
    cout<<a<<endl;

    }
    else{
        cout<<a<<endl;
    }

    // lower to upper whole string

    string c = "sarthak";
    for(int i=0;i<c.size();i++){
        if(c[i]>='a' && c[i]<= 'z'){
            c[i] -= 32;
            cout<<c[i];
        }
        else{
            cout<<c[i];
        }
    }
    cout<<endl;

    //using shortcut
    string d = "SarThAk";
    d[0] = tolower(d[0]);
    cout<<d<<endl; 

}