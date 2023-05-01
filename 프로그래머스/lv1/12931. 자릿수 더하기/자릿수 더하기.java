import java.util.*;

public class Solution {
    public int solution(int n) {
        
        char[] charArray = Integer.toString(n).toCharArray();
        int sum = 0;
        for (int i = 0; i < charArray.length; i++ ) {
            sum += charArray[i] - '0';
        }

        return sum;
    }
}