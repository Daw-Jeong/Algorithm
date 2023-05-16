import java.util.*;
class Solution {
    public String[] solution(String my_string) {
        String[] answer = new String[my_string.length(
)];
        // ArrayList<String> arr = new ArrayList<String>();
        // for (int i = 0; i < my_string.length(); i++) {
        //     arr.add(my_string.substring(my_string.length()-i-1));
        // }
        // answer = arr.toArray(new String[0]);
        
        for (int i = 0; i < my_string.length(); i++) {
            answer[i] = my_string.substring(my_string.length()-i-1);
        }
        
        Arrays.sort(answer);
        
        return answer;
    }
}