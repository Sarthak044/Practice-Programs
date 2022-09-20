#include<iostream>
#include<string>
using namespace std;

int main(){
    // If you are given a string of digits and asked to calculate the sum of those digits in the string this is the way

    string s1 = "1234";
    // Calculate the sum of these digits
    int sum = 0;
    for(int i = 0; i<s1.size(); i++ ){
        sum += s1[i] - '0';
    } 
    cout<<sum<<endl;
    // the string '0' here signifies the value 48 to be subtracted from the given sum. 0 = 48 in ASCII
}