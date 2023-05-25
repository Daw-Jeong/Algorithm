import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        Integer[] arrInt = Arrays.stream(arr).boxed().toArray(Integer[]::new);
        
        boolean found = Arrays.asList(arrInt).contains(2);
        if(!found) {
            return new int[]{-1};
            }
        
        int first = 0;
        int last = 0;
        
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 2) {
                first = i;
                break;
            }
        }
        
        for (int j = arr.length-1; j >= 0; j--) {
            if (arr[j] == 2) {
                last = j;
                break;
            }
        }
        
        int[] answer = Arrays.copyOfRange(arr, first, last + 1);

        return answer;
    }
}