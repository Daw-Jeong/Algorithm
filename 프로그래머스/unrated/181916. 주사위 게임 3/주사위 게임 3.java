import java.lang.Math;
import java.util.*;
class Solution {
    public int solution(int a, int b, int c, int d) {
        int answer = 0;
        int[] intArr = new int[]{a,b,c,d};
        //다 다른경우
        if (a != b && b != c && c != d && a != c && a != d && b != d) {
            return Arrays.stream(intArr).min().getAsInt();
        }
        
        if (a == b || b == c || c == d || a == c || a == d || b == d) {
            if (a == b && b == c) {
                if (a == b && b == c && c == d) return 1111 * a;
                else return (10 * a + d)*(10 * a + d);       
            }
            if (a == b && b == d) {
                if (a == b && b == c && c == d) return 1111 * a;
                else return (10 * a + c)*(10 * a + c); 
            }
            if (d == b && b == c) {
                if (a == b && b == c && c == d) return 1111 * a;
                else return (10 * b + a)*(10 * b + a);
            }
             if (a == c && d == c) {
                if (a == b && b == c && c == d) return 1111 * a;
                else return (10 * a + b)*(10 * a + b);
            }
            
            
            //두개씩 같은값
            if (a == b && c == d)
                return (a + c) * Math.abs(a - c);
            else if (a == c && b == d)
                return (a + b) * Math.abs(a - b);
            else if (a == d && b == c)
                return (a + b) * Math.abs(a - b);
            
            
            //두개 같고 나머지 다름
            else if (a == b && c != d) return c * d;
            else if (a == c && b != d) return b * d;
            else if (a == d && b != d) return c * b;
            else if (b == c && a != d) return a * d;
            else if (b == d && c != a) return c * a;
            else return a * b;
            
                     
        }
        
        return answer;
    }
}