import java.util.*;
class Solution {
    public int[] solution(int l, int r) {
//         ArrayList<Integer> arr = new ArrayList<Integer>();
//         for (int i = l; i <= r; i++) {
//             char[] charArr = Integer.toString(i).toCharArray();
//             int temp = 0;
//             for (int j = 0; j < charArr.length; j++) {
                
//                 if (charArr[j] != '5' && charArr[j] != '0') break;
//                 else temp++;
                
//                 if (temp == charArr.length) {
//                     String str = new String(charArr);
//                     arr.add(Integer.valueOf(str));
//                 }
//             }

//         }
//         if (arr.isEmpty()) return new int[]{-1};
        
//         int[] answer = arr.stream().mapToInt(n -> n).toArray();
//         return answer;
        
        ArrayList<Integer> arrList = new ArrayList<>();
        
        for (int i = 1; i < 64; i++) {
            int fiveBinary = Integer.parseInt(Integer.toBinaryString(i))*5;
            if (fiveBinary >= l && fiveBinary <=r) {
                arrList.add(fiveBinary);
            }
        }
        
        return arrList.isEmpty() ? new int[]{-1} : arrList.stream().mapToInt(n -> n).toArray();
    }
}