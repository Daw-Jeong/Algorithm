class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        String sumA = Integer.toString(a) + Integer.toString(b);
        String sumB = Integer.toString(b) + Integer.toString(a);
        
        
        return Integer.parseInt(sumA) > Integer.parseInt(sumB)? Integer.parseInt(sumA) : Integer.parseInt(sumB);
    }
}