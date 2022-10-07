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
