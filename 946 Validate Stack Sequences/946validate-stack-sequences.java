import java.util.Stack;

class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
       Stack<Integer> stack = new Stack<Integer>();
       int j = 0;

       for (int val: pushed) {
           stack.push(val);
           while(j < pushed.length && !stack.isEmpty() && popped[j] == stack.peek()) {
               stack.pop();
               j++;
           }
       }

       return stack.isEmpty();
    }
}