# Leet code question Rectangle Overlap
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        # Unpack coordinates for rectangle 1
        # rec1 = [x1, y1, x2, y2] where (x1, y1) is bottom-left and (x2, y2) is top-right
        x1, y1, x2, y2 = rec1
        
        # Unpack coordinates for rectangle 2
        # rec2 = [x3, y3, x4, y4] where (x3, y3) is bottom-left and (x4, y4) is top-right
        x3, y3, x4, y4 = rec2
        
        # Check if rectangles don't overlap horizontally
        # If rec1's right edge is at or left of rec2's left edge (x2 <= x3)
        # OR rec2's right edge is at or left of rec1's left edge (x4 <= x1)
        # then there's no horizontal overlap
        if x2 <= x3 or x4 <= x1:
            return False
        
        # Check if rectangles don't overlap vertically
        # If rec1's top edge is at or below rec2's bottom edge (y2 <= y3)
        # OR rec2's top edge is at or below rec1's bottom edge (y4 <= y1)
        # then there's no vertical overlap
        if y2 <= y3 or y4 <= y1:
            return False
        
        # If both horizontal and vertical overlap exist, rectangles overlap
        return True
