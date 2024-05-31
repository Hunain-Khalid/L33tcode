# Name : Hunain Khalid
# This code below is the optimized solution for https://leetcode.com/problems/two-sum/
# The question requries us to find two numbers that equal the target value
# TODO: clean up logging and create more modular tests

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
            #target = value + nums[i]
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
"""
class Test1:           
    s = Solution();
    target1:int = 6
    target2:int = 9
    numList1:List[int] = [2,7,11,15]
    numList2:List[int] = [3,2,5,4]
    numList3:List[int] = [3,3,6]

    logger.info("List1 contains %s and target [%s] ", numList1, target2)
    logger.info("List2 contains %s and target [%s] ", numList2, target1)
    logger.info("List3 contains %s and target [%s] ", numList3, target1)
    
    logger.info("Solution to list 1 are values in locations %s added is %s", s.twoSum(numList1,target2), target2)
    logger.info("Solution to list 2 are values in locations %s added is %s", s.twoSum(numList2,target1), target1)
    logger.info("Solution to list 3 are values in locations %s added is %s", s.twoSum(numList3,target1), target1)


class TestSum():           
    def test_pass():
       
        numList1:List[int] = [2,7,11,15]
        

        assert Solution.twoSum(numList1,9) == 9
        logger.info("List1 contains %s and target [%s] ", numList1, 9)

    def test_fail():
       
        numList1:List[int] = [3,2,5,4]

        assert Solution.twoSum(numList1,9) == 100
        logger.info("List1 contains %s and target [%s] but no two values could be found", numList1, 9)
"""



     