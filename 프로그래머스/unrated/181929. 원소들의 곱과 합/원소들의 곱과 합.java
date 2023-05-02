class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        long multiplication = 1;
        long sum = 0;
        for (int i : num_list) {
            multiplication *= i;
            sum += i;
        }
        
        return multiplication < sum*sum ? 1 : 0;
    }
}