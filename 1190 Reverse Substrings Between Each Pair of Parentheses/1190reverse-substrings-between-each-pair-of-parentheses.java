import java.util.Stack;

class Solution {
    private String[] reverseString(String s, int start) {
        Stack<Character> reversed = new Stack<Character>();
        String res = "";
        int i = start + 1;

        while (i < s.length() && s.charAt(i) != ')')  {
            if (s.charAt(i) == '(') {
                String[] tmp = reverseString(s, i);
                for (int j = 0; j < tmp[0].length(); j++) {
                    reversed.push(tmp[0].charAt(j));
                }
                i = Integer.parseInt(tmp[1]);
            }
            else {
                reversed.push(s.charAt(i));
                i++;
            }
        }

        while (reversed.size() > 0) {
            res += reversed.pop();
        }

        String[] returnValue = {res, Integer.toString(i + 1)};

        return returnValue;
    }
    public String reverseParentheses(String s) {
        String finalString = "";
        int i = 0;

        while (i < s.length()) {
            if (s.charAt(i) == '(') {
                String[] res = reverseString(s, i);
                finalString += res[0];
                i = Integer.parseInt(res[1]);
            } else {
                finalString += s.charAt(i);
                i++;
            }
        }

        return finalString;
    }
}
