class Solution {
    public boolean solution(int x) {
//         boolean answer = true;
        
//         int sum = 0;
//         for (int rest = x; rest > 0; rest /= 10) {
//             sum += rest % 10;
//         }
//         if (x % sum != 0) {
//             answer = false;
//         }
    
//         return answer;
        
        int sum = String.valueOf(x).chars().map(eachChar -> eachChar - '0').sum();
        return x % sum == 0;
    }
}