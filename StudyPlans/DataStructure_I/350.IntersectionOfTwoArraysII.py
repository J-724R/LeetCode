# Two Pointers
class Solution:
    def intersect(nums1, nums2):
      # Both arrays needs to be sorted
      nums1.sort()
      nums2.sort()

      # Init pointers, helpers for the iteration
      i = 0 ; j = 0

      # Create output list
      intersections = [] 

      # Compare simultaneusly
      while i < len(nums1) and j < len(nums2):
        # Transvers firts array seeking for a match, then transverse second array
        # Only posible to cover all case if the arrays are sorted 
        if (nums1[i] < nums2[j]):
           i += 1
        elif (nums1[i] > nums2[j]):
           j += 1
        else:
           intersections.append(nums1[i])
           i += 1
           j += 1
      
      return intersections
    
# Hash table
class Solution:
    def intersect(nums1, nums2):
      #  Create hash table, keys will be used for comparision and values to store how many times each number appears 
      hash = {}
      for num in nums1:
        hash[num] = hash.get(num, 0) +1

      intersections = []

      # Compare each element of second array with the keys in the hashmap
      for num in nums2:
         if num in hash and hash[num] > 0:
            intersections.append(num)
            hash[num] -= 1 

      return intersections


            
