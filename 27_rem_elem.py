"""
 Name : Hunain Khalid
 This code below is the optimized solution for 
 https://leetcode.com/problems/remove-element/
 The problem requires us to remove all occurences of 
 value in numbers array in-place, returining number of elements
 which are not equal to value.

 Solution explanation 
 '''1. return number of elements in nums not equal to val'''
 
"""
from typing import List
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')

#Create array nums sorted ex. nums=[0,0,1,1,1,2,2,3,3,4], 5 arr=
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''1.Going to use 2 ptr solution first pointer =
             right pointer = rp, 2nd pointer = left pointer =
        '''
        lp = 0
        
        for rp in range (0, len(nums)):
            if nums[rp] != val:
                nums[rp] = nums[lp]
                lp += 1

        return lp
    

import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first(self):
        self.assertEqual(
            self.solution.removeElement(nums=[3, 2, 2, 3], val=3),
            2,
        )
    logger.info("Test_first: %s, %s, : %s", 
                'nums=[3, 2, 2, 3]', 'val=2', 'sol=2')
    

if __name__ == "__main__":
    unittest.main()    



     