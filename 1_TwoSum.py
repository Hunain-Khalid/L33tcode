"""
 Name : Hunain Khalid
 This code below is the optimized solution for https://leetcode.com/problems/two-sum/
 The question requries us to find two numbers that equal the target value
"""
from typing import List
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        keyValPairs = {}
        n = len(nums)

        for i in range (n):
            #target = value asds+ nums[i]
            value = target - nums[i]
            if value in keyValPairs:
                return [keyValPairs[value], i]
            keyValPairs[nums[i]] = i
        
        return []
    

import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first(self):
        self.assertEqual(
            self.solution.twoSum(nums=[2, 7, 11, 15], target=9),
            [0, 1],
        )
    logger.info("Test_first: %s, %s, : %s", 
                'nums=[2, 7, 11, 15]', 'target=9', 'sol=[0,1]')

    def test_second(self):
        self.assertEqual(
            self.solution.twoSum(nums=[3, 2, 4], target=6),
            [1, 2],
        )
    logger.info("Test_second: %s, %s, : %s",
                 'nums=[3, 2, 4]', 'target=6', 'sol=[1,2]')

if __name__ == "__main__":
    unittest.main()    



     