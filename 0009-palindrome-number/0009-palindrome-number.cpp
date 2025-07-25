class Solution {
public:
    bool isPalindrome(int x) {
       if (x<0 || ( x % 10 == 0 && x!= 0)) {
            return false;
        }

        if (x<10) return true;

        int original= x;
        long long rev=0;

        while (x>0){
            rev= rev*10 + x % 10;
            x /=10;
        }

        return original==rev;  
    }
};