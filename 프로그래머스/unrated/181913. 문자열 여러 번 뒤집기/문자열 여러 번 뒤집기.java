import java.util.*;
class Solution {
    public String solution(String my_string, int[][] queries) {
        String answer = "";
        String[] strArr = my_string.split("");
        //어떻게 뒤집어서 저장 arrray.reverse() 로?
        for (int i = 0; i < queries.length; i++) {
            String[] copyArr = Arrays.copyOfRange(strArr,queries[i][0],queries[i][1]+1);
            List<String> strList = Arrays.asList(copyArr);
            Collections.reverse(strList);
            copyArr = strList.toArray(copyArr);
            System.arraycopy(copyArr, 0, strArr, queries[i][0], queries[i][1] - queries[i][0] + 1);

        }
        for (String str : strArr) {
            answer += str;
        }

        return answer;
    }
}