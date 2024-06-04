"""
 Name : Hunain Khalid
 This code below is the optimized solution for 
 https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
 The problem requires us to remove duplicates from a sorted array

 Solution explanation TODO
 '''2 pointer solution rgt_ptr goes through
        # one by one while lft_ptr stays at its
        # index (anchor), start both at 1 
        this is a look forward 1 algo you need
        to compare right pointer with the value 
        immediatley ahead of it current value subtract 1 and start at 1
        i was comparing the ptrs against each other this was wrong
        [rgt_ptr - 1, rgt_ptr] is a good visual when comparing '''
"""
from typing import List
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')

#Create array nums sorted ex. nums=[0,0,1,1,1,2,2,3,3,4], 5 arr=
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''#look up table not needed, use 2 pointers for
        #in place solution '''
        lft_ptr = 1
        
        for rgt_ptr in range (1, len(nums)):
            if nums[rgt_ptr] != nums[rgt_ptr - 1]:
                nums[lft_ptr] = nums[rgt_ptr]
                lft_ptr += 1
        
        return lft_ptr
    

import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first(self):
        self.assertEqual(
            self.solution.removeDuplicates(nums=[0,0,1,1,1,2,2,3,3,4]), 5)
    logger.info("Test_first: %s : %s", 
                'nums=[0,0,1,1,1,2,2,3,3,4]', 'sol=5, nums=[0,1,2,3,4,_,_,_,_]')
    '''
    def test_second(self):
        self.assertEqual(
            self.solution.twoSum(nums=[3, 2, 4], target=6),
            [1, 2],
        )
    logger.info("Test_second: %s, %s, : %s",
                 'nums=[3, 2, 4]', 'target=6', 'sol=[1,2]')
    '''
if __name__ == "__main__":
    unittest.main()    



     