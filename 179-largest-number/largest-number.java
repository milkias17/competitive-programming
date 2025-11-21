import java.util.Arrays;

class Solution {

    public String largestNumber(int[] nums) {
        String[] stringArray = Arrays.stream(nums)
                                     .mapToObj(String::valueOf)
                                     .toArray(String[]::new);
        
        Arrays.sort(stringArray, (s1, s2) -> {
            String tmp1 = s2 + s1;
            String tmp2 = s1 + s2;
            return tmp1.compareTo(tmp2);

        });

        String result = String.join("", stringArray);
        if (result.charAt(0) == '0') {
            return "0";
        }
        return result;
    }
}