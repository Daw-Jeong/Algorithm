import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        //queries 돌면서 s,e,k 찾고
        for (int n = 0; n < queries.length; n++ ) {
            
            int s = queries[n][0];
            int e = queries[n][1];
            int k = queries[n][2];
            
            ArrayList<Integer> biggerThanK = new ArrayList<Integer>(); 
            //s <= i <= e k보다 큰 arraylist
            for ( int i = s; i <= e; i++ ) {
                if ( arr[i] > k ) {
                    biggerThanK.add(arr[i]);
                }
            }
            if ( biggerThanK.isEmpty() ) answer[n] = -1;
            else answer[n] = Collections.min(biggerThanK);
        }
        return answer;
    }
}