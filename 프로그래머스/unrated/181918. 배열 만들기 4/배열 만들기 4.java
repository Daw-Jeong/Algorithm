import java.util.*;
class Solution {
    public int[] solution(int[] arr) {
//         ArrayList<Integer> stk = new ArrayList<Integer>();
//         int i = 0;
//         while (i < arr.length) {
//             if (stk.isEmpty()) {
//                 stk.add(arr[i]);
//                 i++;
//             }
//             else {
//                 if (stk.get(stk.size()-1) < arr[i]) {
//                     stk.add(arr[i]);
//                     i++;
//                 }
//                 else stk.remove(stk.size()-1);
//             }
//         }
        
//         int[] answer = stk.stream().mapToInt(l -> l).toArray();
//         return answer;
        int i = 0;
        Stack<Integer> stk = new Stack<>();
        
        while (i < arr.length) {
            if (stk.isEmpty()) {
            stk.push(arr[i]);
            i++;
            }
            else {
                if (stk.peek() < arr[i]) {
                  stk.push(arr[i]);
                  i++;
              }
                else {
                 stk.pop();
                }
            }
        }
        
        int[] answer = stk.stream().mapToInt(l -> l).toArray();
        return answer;
        
    }
}