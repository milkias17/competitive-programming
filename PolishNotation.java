import java.util.Stack;
import java.util.ArrayList;

class Solution {
    private boolean isOperator(String s) {
        String[] operators = {"+", "*", "/", "-"};
        for (String operator: operators) {
            if (operator.equals(s)) {
                return true;
            }
        }

        return false;
    }
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<Integer>();
        for (String s: tokens) {
            if (!this.isOperator(s)) {
                stack.push(Integer.parseInt(s));
            }
            else {
                int secondEl = stack.pop();
                int firstEl = stack.pop();
                switch (s) {
                    case "+":
                        stack.push(firstEl + secondEl);
                        break;
                    case "-":
                        stack.push(firstEl - secondEl);
                        break;
                    case "*":
                        stack.push(firstEl * secondEl);
                        break;
                    case "/":
                        stack.push(firstEl / secondEl);
                    default:
                        break;
                }
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
        System.out.println(sol.evalRPN(tokens2));
    }
}
