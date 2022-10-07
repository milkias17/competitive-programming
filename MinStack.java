import java.util.ArrayList;

class MinStack {
    private ArrayList<Integer> stack;
    private ArrayList<Integer> minList;

    public MinStack() {
        stack = new ArrayList<Integer>();
        minList = new ArrayList<Integer>();
    }
    
    public void push(int val) {
        if (minList.size() == 0) {
            minList.add(val);
        } else if (val <= minList.get(minList.size() - 1)) {
            minList.add(val);
        }
        stack.add(val);
    }
    
    public void pop() {
        int val = stack.get(stack.size() - 1);
        if (minList.get(minList.size() - 1) == val) {
            minList.remove(minList.size() - 1);
        }
        stack.remove(stack.size() - 1);
    }
    
    public int top() {
        return stack.get(stack.size() - 1);
    }
    
    public int getMin() {
        return minList.get(minList.size() - 1);
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
