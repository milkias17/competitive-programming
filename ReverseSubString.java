import java.util.Stack;

/**
    You are given a string s that consists of lower case English letters
    and brackets.

    Reverse the strings in each pair of matching parentheses, starting from
    the innermost one.

    Your result should not contain any brackets.

    Example 1:
    Input: s = "(abcd)" Output: "dcba"

    Example 2:
    Input: s = "(u(love)i)" Output: "iloveu" Explanation: The substring
    "love" is reversed first, then the whole string is reversed.

    Example 3:
    Input: s = "(ed(et(oc))el)" Output: "leetcode" Explanation: First,
    we reverse the substring "oc", then "etco", and finally, the whole string.
 **/

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

public class ReverseSubString {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.reverseParentheses("(abcd)"));
        System.out.println(sol.reverseParentheses("(u(love)i)"));
        System.out.println(sol.reverseParentheses("(ed(et(oc))el)"));
        System.out.println(sol.reverseParentheses("s()uteawj((eg))"));
    }
}
