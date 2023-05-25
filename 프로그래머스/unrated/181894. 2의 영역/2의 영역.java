import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(int[] arr) {
        
        int[] idxArr = IntStream.range(0, arr.length).filter(i -> arr[i] == 2).toArray();
        if (idxArr.length == 0) return new int[]{-1};
        
        return IntStream.rangeClosed(idxArr[0],idxArr[idxArr.length-1]).map(j -> arr[j]).toArray();
        
//         Integer[] arrInt = Arrays.stream(arr).boxed().toArray(Integer[]::new);
        
//         boolean found = Arrays.asList(arrInt).contains(2);
//         if(!found) {
//             return new int[]{-1};
//             }
        
//         int first = 0;
//         int last = 0;
        
//         for (int i = 0; i < arr.length; i++) {
//             if (arr[i] == 2) {
//                 first = i;
//                 break;
//             }
//         }
        
//         for (int j = arr.length-1; j >= 0; j--) {
//             if (arr[j] == 2) {
//                 last = j;
//                 break;
//             }
//         }
        
//         int[] answer = Arrays.copyOfRange(arr, first, last + 1);

//         return answer;
    }
}