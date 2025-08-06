--# Intuition
-- Left join as the output is the left table enriched with address fields instead of being filtered by only those values having an address -->

--# Approach
-- left join on person id from both tables-->

--# Complexity
--m is number of rows in Person

-- Time complexity: 
--Metric			With Index		Without Index
--Time Complexity	O(n × log m)	O(n × m) (nested)

-- Space complexity: O(N)
--Space Complexity		O(m) (hash join)	O(n + m) (merge on sorted tables)


# Code

def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
	a, b, write_index = m-1, n-1, m + n - 1

	while b >= 0:
		if a >= 0 and nums1[a] > nums2[b]:
			nums1[write_index] = nums1[a]
			a -= 1
		else:
			nums1[write_index] = nums2[b]
			b -= 1

		write_index -= 1