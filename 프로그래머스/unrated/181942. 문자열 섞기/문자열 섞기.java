class Solution {
    public String solution(String str1, String str2) {
        String answer = "";
        // char[] charArr1 = str1.toCharArray();
        // char[] charArr2 = str2.toCharArray();
        
        // for (int i = 0; i < str1.length(); i++) {
        //     answer = answer + charArr1[i] + charArr2[i];
        // }
        for (int i = 0; i < str1.length(); i++) {
            answer = answer + str1.charAt(i) + str2.charAt(i);
        }
        return answer;
    }
}