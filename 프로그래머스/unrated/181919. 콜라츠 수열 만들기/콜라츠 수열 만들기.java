import java.util.ArrayList;

class Solution {
    public int[] solution(int n) {
        ArrayList<Integer> answer = new ArrayList<Integer>();
        
        while (n != 1) {
            answer.add(n);
            if (n % 2 == 0) {
                n /= 2;
            }
            else {
                n = 3 * n + 1;
            }
                
        }
        answer.add(1);
        //Integer를 int 타입으로 바꿔야 가능
        return answer.stream()
                .mapToInt(Integer::intValue)
                .toArray();
    }
}