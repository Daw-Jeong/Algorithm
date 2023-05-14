import java.util.*;

class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        
        ArrayList<Integer> answer = new ArrayList<Integer>();
        
        for (String str : intStrs) {
            
            String temp = str.substring(s, s+l);
            int tempInt = Integer.parseInt(temp);
            
            if (tempInt > k) {
                answer.add(tempInt);    
            }
        }
        
        return answer.stream().mapToInt(i->i).toArray();
    }
}