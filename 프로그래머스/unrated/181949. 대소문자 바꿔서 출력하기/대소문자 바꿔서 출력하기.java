import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        char[] charArr = a.toCharArray();
        for (int i = 0; i < charArr.length; i++) {
            char temp = charArr[i];
            if (Character.isUpperCase(temp)) {
                charArr[i] = Character.toLowerCase(temp);
            }
            else {
                charArr[i] = Character.toUpperCase(temp);
            }
        }
        // String answer = new String(charArr);
        System.out.print(new String(charArr));
    }
}