class Solution {
    public String solution(int q, int r, String code) {
//         String answer = "";
        
//         for (int i = 0; i < code.length(); i++) {
            
//             if (i % q == r) answer += code.charAt(i);
            
//         }
        
//         return answer;
        
        
        StringBuilder strBuilder = new StringBuilder();
                for (int i = 0; i < code.length(); i++) {
            
            if (i % q == r) strBuilder.append(code.charAt(i));
            
        }
        
        return strBuilder.toString();
        
    }
}