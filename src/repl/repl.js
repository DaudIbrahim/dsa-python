
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {

    const result = []
    // console.log(target)


    for (let i = 0; i < nums.length; i++) {
        const elementInner = nums[i];

        for (let j = i + 1; j < nums.length; j++) {
            const elementOuter = nums[j];

            if ((elementInner + elementOuter) === target) {
                result.push(i)
                result.push(j)
                return result
            }

        }

    }


    return result
};



const result = twoSum([2, 7, 11, 15], 9)
console.log(result)


