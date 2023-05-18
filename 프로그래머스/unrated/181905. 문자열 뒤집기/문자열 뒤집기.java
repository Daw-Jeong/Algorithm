class Solution {
    public String solution(String my_string, int s, int e) {
        
        StringBuilder answer = new StringBuilder(my_string);
        StringBuilder temp = new StringBuilder(my_string.substring(s, e+1));
        temp.reverse();
        answer.replace(s, e+1, temp.toString());
        
        return answer.toString();
    }
}