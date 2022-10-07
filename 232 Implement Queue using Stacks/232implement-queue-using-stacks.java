import java.util.Stack;

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */

class MyQueue {
    private Stack<Integer> stack;
    private int size;

    public MyQueue() {
        stack = new Stack<Integer>();
        size = 0;
    }
    
    public void push(int x) {
        if (stack.empty()) {
            stack.push(x);
        } else {
            int[] values = new int[size];
            for (int i = 0; i < size; i++) {
                values[i] = stack.pop();
            }
            stack.push(x);
            for (int i = size - 1; i >= 0; i--) {
                stack.push(values[i]);
            }
        }
        size++;
    }
    
    public int pop() {
        size--;
        return stack.pop();
    }
    
    public int peek() {
        return stack.peek();
    }
    
    public boolean empty() {
        return size == 0;
    }
}

