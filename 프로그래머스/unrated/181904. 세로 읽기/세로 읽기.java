class Solution {
    public String solution(String my_string, int m, int c) {
        String answer = "";

        String[] strArr = new String[my_string.length()/m];
        for (int i = 0; i < strArr.length; i++) {
            strArr[i] = my_string.substring(i*m, (i+1)*m);
            answer += strArr[i].charAt(c-1);
        }

        return answer;
    }
}