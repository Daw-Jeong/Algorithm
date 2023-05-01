class Solution {
    public int solution(int a, int b) {
        
//         String sum = Integer.toString(a) + Integer.toString(b);
        
//         return Integer.valueOf(sum) > 2*a*b ?
//             Integer.valueOf(sum) : 2*a*b;
        
        int ab = Integer.parseInt(a + "" + b);
        return ab >2*a*b ? ab : 2*a*b;
    }
}