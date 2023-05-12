import java.lang.Math;
import java.util.*;
class Solution {
    public int solution(int a, int b, int c, int d) {
        int answer = 0;
        int[] intArr = new int[]{a,b,c,d};
        
        if (a == b && b == c && c == d) {
            return a * 1111;
        }
        
        
        else if (a == b && b == c) {
            return threeSame(a, b, c, d);
        }
        else if (a == b && b == d) {
            return threeSame(a, b, d, c);
        }
        else if (a == c && d == c) {
            return threeSame(a, c, d, b);
        }
        else if (d == b && b == c) {
            return threeSame(d, b, c, a);
        }
        
        
        
        else if (a == b && c == d) {
            return eachTwoSame(a, c);
        }
        else if (a == c && b == d) {
            return eachTwoSame(a, b);
        }
        else if (a == d && b == c) {
            return eachTwoSame(a, b);
        }
        
        
        
        else if (a == b) {
            return justTwoSame(c, d);
        }
        else if (a == c) {
            return justTwoSame(b, d);
        }
        else if (a == d) {
            return justTwoSame(b, c);
        }
        else if (b == c) {
            return justTwoSame(a, d);
        }
        else if (b == d) {
            return justTwoSame(a, c);
        }
        else if (c == d) {
            return justTwoSame(a, b);
        }
        
        
        else return Math.min(Math.min(a,b), Math.min(c,d));
        
    }
        

        
        int threeSame(int x, int y, int z, int m) {
            return (10 * x + m)*(10 * x + m);
        }
        
        int eachTwoSame(int x, int y) {
            return (x + y) * Math.abs(x - y);
        }
        
        int justTwoSame(int x, int y) {
            return x * y;
        }
        
        
        
//         int[] intArr = new int[]{a,b,c,d};
//         //다 다른경우
//         if (a != b && b != c && c != d && a != c && a != d && b != d) {
//             return Arrays.stream(intArr).min().getAsInt();
//         }
        
//         if (a == b || b == c || c == d || a == c || a == d || b == d) {
//             if (a == b && b == c) {
//                 if (a == b && b == c && c == d) return 1111 * a;
//                 else return (10 * a + d)*(10 * a + d);       
//             }
//             if (a == b && b == d) {
//                 if (a == b && b == c && c == d) return 1111 * a;
//                 else return (10 * a + c)*(10 * a + c); 
//             }
//             if (d == b && b == c) {
//                 if (a == b && b == c && c == d) return 1111 * a;
//                 else return (10 * b + a)*(10 * b + a);
//             }
//              if (a == c && d == c) {
//                 if (a == b && b == c && c == d) return 1111 * a;
//                 else return (10 * a + b)*(10 * a + b);
//             }
            
            
//             //두개씩 같은값
//             if (a == b && c == d)
//                 return (a + c) * Math.abs(a - c);
//             else if (a == c && b == d)
//                 return (a + b) * Math.abs(a - b);
//             else if (a == d && b == c)
//                 return (a + b) * Math.abs(a - b);
            
            
//             //두개 같고 나머지 다름
//             else if (a == b && c != d) return c * d;
//             else if (a == c && b != d) return b * d;
//             else if (a == d && b != d) return c * b;
//             else if (b == c && a != d) return a * d;
//             else if (b == d && c != a) return c * a;
//             else return a * b;
            
                     
//         }
        
        // return answer;
   
}