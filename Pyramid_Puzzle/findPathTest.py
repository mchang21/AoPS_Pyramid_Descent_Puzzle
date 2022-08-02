import unittest
from pyramid import Pyramid

# Test findPath function in Pyramid class
class TestFindPath(unittest.TestCase):

    # Test case where there is a path to return
    def testNormalCase(self):
        p1 = Pyramid([[1],
                     [2,3],
                    [4,1,1]])
        self.assertEqual(p1.findPath(2), "LR")
        self.assertEqual(p1.findPath(3), "RL")
        self.assertEqual(p1.findPath(8), "LL")

        p2 = Pyramid([[2],
                     [4,3],
                    [3,2,6],
                   [2,9,5,2],
                 [10,5,2,15,5]])

        self.assertEqual(p2.findPath(720), "LRLL")
        self.assertEqual(p2.findPath(120), "RLRL")
        self.assertEqual(p2.findPath(360), "RRLL")

    # Test case where no path exists
    def testNoPathFound(self):
        p1 = Pyramid([[1],
                     [2,3],
                    [4,1,1]])
        self.assertEqual(p1.findPath(1), "")
        self.assertEqual(p1.findPath(4), "")
        self.assertEqual(p1.findPath(6), "")

        p2 = Pyramid([[2],
                     [4,3],
                    [3,2,6],
                   [2,9,5,2],
                 [10,5,2,15,5]])

        self.assertEqual(p2.findPath(1000), "")
        self.assertEqual(p2.findPath(8), "")
        self.assertEqual(p2.findPath(721), "")

# Run the tests
unittest.main()