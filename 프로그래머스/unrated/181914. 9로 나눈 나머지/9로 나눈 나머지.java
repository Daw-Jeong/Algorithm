class Solution {
    public int solution(String number) {
        int answer = 0;
        int sum = 0;
        String[] strArr = number.split("");
        for (String str : strArr) {
            sum += Integer.valueOf(str);
        }
        answer = sum % 9;
        return answer;
    }
}