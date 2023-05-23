import java.util.*;

class Solution {
    public int[] solution(int n, int[] slicer, int[] num_list) {
        
        if (n == 1) {
            return Arrays.copyOfRange(num_list, 0, slicer[1]+1);            
        }
        
        else if (n == 2) {
            return Arrays.copyOfRange(num_list, slicer[0], num_list.length); 
        }
        
        else if (n == 3) {
            return Arrays.copyOfRange(num_list, slicer[0], slicer[1]+1); 
        }
        
        else {
            int[] temp = Arrays.copyOfRange(num_list, slicer[0], slicer[1]+1);
            ArrayList<Integer> arr = new ArrayList<Integer>();
            for (int i = 0; i < temp.length; i += slicer[2]) {
                arr.add(temp[i]);
            }

            return arr.stream().mapToInt(i -> i).toArray();
        }

    }
}