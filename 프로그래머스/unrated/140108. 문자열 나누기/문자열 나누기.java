class Solution {
    public int solution(String s) {
        int answer = 0;
            String sub = s;
            char firstChar = s.charAt(0);

            //첫째 문자 count
            int firstCharCount = 0;
            //다른 문자 count
            int diffCharCount = 0;

            while (sub.length() > 0) {
                if (firstCharCount > 0 && firstCharCount == diffCharCount) {
                    answer ++;
                    sub = sub.substring(firstCharCount*2);
                    firstCharCount = 0;
                    diffCharCount = 0;
                    continue;
                }
                else if (firstCharCount > 0 && firstCharCount != diffCharCount) {
                    if (firstCharCount + diffCharCount == sub.length()){
                        answer ++;
                        break;
                    }
                    else if (sub.charAt(firstCharCount + diffCharCount) != firstChar) {
                        diffCharCount ++;
                        continue;
                    }
                    else {
                        firstCharCount ++;
                        continue;
                    }
                }

                firstChar = sub.charAt(0);
                firstCharCount ++;

            }
            return answer;
    }
}