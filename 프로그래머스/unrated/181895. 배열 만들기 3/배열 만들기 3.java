import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[][] intervals) {

        ArrayList<Integer> arrList = new ArrayList<Integer>();
        for (int i = intervals[0][0]; i <= intervals[0][1]; i++) {
           arrList.add(arr[i]); 
        }
        
        for (int j = intervals[1][0]; j <= intervals[1][1]; j++) {
           arrList.add(arr[j]); 
        }
        int[] answer = arrList.stream().mapToInt(i -> i).toArray();
        return answer;
    }
}