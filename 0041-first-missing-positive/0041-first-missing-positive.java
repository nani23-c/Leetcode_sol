class Solution {
    public int firstMissingPositive(int[] nums) {
        Set <Integer> hset = new HashSet<>();
        for(int x:nums){
            hset.add(x);
        }
        int i = 1;
        while(hset.contains(i)){
            i+=1;
        }
        return i;
    }
}