import java.util.Stack;
import java.util.ArrayList;

class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<Integer>();
        for (String s: tokens) {
            int firstEl;
            int secondEl;
            switch (s) {
                case "+":
                    secondEl = stack.pop();
                    firstEl = stack.pop();
                    stack.push(firstEl + secondEl);
                    break;
                case "-":
                    secondEl = stack.pop();
                    firstEl = stack.pop();
                    stack.push(firstEl - secondEl);
                    break;
                case "*":
                    secondEl = stack.pop();
                    firstEl = stack.pop();
                    stack.push(firstEl * secondEl);
                    break;
                case "/":
                    secondEl = stack.pop();
                    firstEl = stack.pop();
                    stack.push(firstEl / secondEl);
                    break;
                default:
                    stack.push(Integer.parseInt(s));
            }
        }
        return stack.pop();
    }
}

public class PolishNotation {
    public static void main(String[] args) {
        Solution sol = new Solution();
        String[] tokens = {"10","6","9","3","+","-11","*","/","*","17","+","5","+"};
        String[] tokens2 = {"2","1","+","3","*"};
        System.out.println(sol.evalRPN(tokens));
    }
}
