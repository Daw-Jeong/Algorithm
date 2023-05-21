import java.util.*;
class Solution {
    public String solution(String my_string, int[] indices) {
        
        StringBuilder answer = new StringBuilder(my_string);
        int subtract = 0;
        
        Arrays.sort(indices);
        
        for (int i = 0; i < indices.length; i++) {
            
            answer.replace(indices[i]-subtract, indices[i]-subtract+1, "");
            subtract++;
            
        }
        
        return answer.toString();
    }
}