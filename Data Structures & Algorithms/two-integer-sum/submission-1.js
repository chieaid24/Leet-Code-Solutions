class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        // first thought is a double for loop, o(n^2)
        // create a set of numbers as you loop through
        // for each, check if it's complement is in the set,
        // if so, return true, if not add num to set
        const complements = new Map();
        
        for (let k = 0; k < nums.length; k++) {
            if (complements.has(target - nums[k])) {
                return [complements.get(target - nums[k]), k];
            }
            complements.set(nums[k], k);
        }
        return false;

    }
}
