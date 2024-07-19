/*
Given an integer x, return true if x is a
palindrome
, and false otherwise.
*/

#include <string>
class Solution {
public:
    bool isPalindrome(int x) {
               std::string str = std::to_string(x);
        bool result = true;
        bool keepon = true;

        for(std::string::size_type i = 0 ; i < str.length() && keepon; i++){
            for(std::string::size_type j = (str.length() - 1) ; j >=0 && keepon; j--){
                  if(str[i] == str[j]){
                        result = true;
                        i++;
                        if(j == 0) keepon = false;
                  }
                  else{
                        result = false;
                        keepon = false;
                  }
            }
        }
        return result;
    }
};
