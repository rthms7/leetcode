class Solution(object):
    def twoSum(self, nums, target):
        """Logic: insert the input array into the hash map. for every element in input array check   if the difference between it and the target is already present in the hash map. if the difference is present then return the index of the input array element and and the index of the differnce in the hash map""" 
        hashmap=[]
        for index,i in enumerate(nums):
            difference=target-i
            if difference in hashmap:
                result=[hashmap.index(difference),index]
                return result
            else:
                hashmap.append(i)


        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        #Initial logic: sort the input array. check if the sum of the largest and smallest element matches the target and traverse from largest to smallest if no match. Return the index positions of the two elements from input list. This approach did not work because after the array was sorted it was difficult to match the index position of elements in the original array without increasing code complexity.
        orig=nums[:]
        nums.sort()
        nums=[ number for number in nums if number<=target]
        flag=False
        for index,i in enumerate(nums[-1::-1]):
            og_index=len(nums)-1-index
            for j in nums[:og_index]:
                if i+j==target:
                    flag=True
                    if i==j:
                        print(i,j)
                        result=[orig.index(i),orig.index(i,orig.index(i)+1)]
                        print(result)
                        return result
                        break
                    result=[orig.index(j),orig.index(i)]
                    return result
                    break
            if flag==True:
                break        
        """