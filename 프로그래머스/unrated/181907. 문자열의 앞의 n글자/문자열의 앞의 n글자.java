class Solution {
    public String solution(String my_string, int n) {
        String answer = "";
        char[] charArr = new char[n];        
        my_string.getChars(0, n, charArr, 0);
        answer = new String(charArr);
        
        return answer;
    }
}