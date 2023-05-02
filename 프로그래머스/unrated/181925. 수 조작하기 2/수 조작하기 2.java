class Solution {
    public String solution(int[] numLog) {
        String answer = "";
        int before = 0;
        
        for (int i = 0; i < numLog.length; i++) {
            
            switch(numLog[i]-before) {
                case 1:
                    answer += "w";
                    break;
                case -1:
                    answer += "s";
                    break;
                case 10:
                    answer += "d";
                    break;
                case -10:
                    answer += "a";
                    break;
                default:
                    break;
            }
            
            before = numLog[i];
        }
        
        return answer;
    }
}