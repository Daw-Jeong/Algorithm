class Solution {
    public int[] solution(String my_string) {
        int[] answer = new int[52];
        
        for (int i = 65; i <= 90; i++) {
            int count = 0;
            for (int l = 0; l < my_string.length(); l++) {
                
                if (my_string.charAt(l) == i) {
                    count++;
                }
            }
            answer[i-65] = count;
        }
        
                for (int i = 97; i <= 122; i++) {
            int count = 0;
            for (int l = 0; l < my_string.length(); l++) {
                
                if (my_string.charAt(l) == i) {
                    count++;
                }
            }
            answer[i-71] = count;
        }
        
        
        
        return answer;
    }
}