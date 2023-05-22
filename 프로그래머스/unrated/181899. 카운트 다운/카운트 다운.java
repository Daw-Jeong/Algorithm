import java.util.stream.*;
class Solution {
    public int[] solution(int start, int end) {
        // int[] answer = new int[start-end+1];
        // int temp = start;
        // for (int i = 0; i < start-end+1; i++) {
        //     answer[i] = temp;
        //     temp--;
        // }
        // return answer;

        return IntStream.rangeClosed(-start, -end).map(n -> -n).toArray();
    }
}