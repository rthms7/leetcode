# Intuition
#<!--First approach was with python sets and its ability to hold only unique elements and possible operations with sets like union and intersection. This approach however was not suited to handling duplicate common elements -->

# Approach
#<!-- Next approach was to use list comprehension. The first element was converted to list of ccharacters and stored. the remaining elements were traversed and each element was compared to contents of first element characters. If the loop letter was not present in the list of first element characters the loop would continue else it would be added to a temp list and simultaneously popped from list of first element characters to avoid matching duplicates. At the end of each iteration of each word in input list, the contents of temp list will override the contents of list of first elemnt characters since the common letters between the first element and element under consideration are stored in the temp list-->

# Complexity
#- Time complexity:
#<!-- $$O( N * M )$$ -->

#- Space complexity:
#<!-- $$O(N) -->

# Code
#```python []
words=['hello','bella','roller'] #->['e','l','l']
class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result_list=list(words[0])

        if len(words)==1:
            return result_list

        for word in words[1:]:
            temp=[]
            for i in word:
                if i not in result_list:
                    continue
                else:
                    temp.append(i)
                    result_list.remove(i)
            result_list=temp[:]
            if not result_list:
                return result_list
                break
        return result_list

#To try: Alternate approach
#        return reduce(and_,map(Counter,w)).elements()