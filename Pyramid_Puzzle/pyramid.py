"""A class to represent a pyramid.

Attributes:
    rows: A list of lists containing integers. Each row is one length longer
     than the previous row, where the first row is of length 1.
"""
class Pyramid:

    """Initiates Pyramid class with a list of rows.

    Args:
        rows: A list of rows representing the pyramid.
    """
    def __init__(self, rows):
        self.rows = rows

    """ Finds a path in the Pyramid whose product is equal to the target.

    Recurses down the entire pyramid from left to right as long as the running
    product is less than the target. 

    Args:
        self: A Pyramid object.
        target: The product of the path to search for.
        parent_idx: The parent index of the current element in the Pyramid.
        current_row_idx: The index of the current Pyramid row.
        current_product: The running product of the current path.
        current_path: A string consisting of "L" or "R" depending on the
            running path.

    Returns:
        The path of the Pyramid whose product is equal to the target. 
        For example, given the following pyramid:

          [1]
         [2,3]
        [4,1,1]

        Target: 8
        Output: "LL"

        Paths which do not exist will return an empty string.
    """
    def findPath(self, target, parent_idx = 0, current_row_idx=1,
     current_product=None, current_path = ""):

        # Sets the initial product to be the number at the top of the pyramid
        if current_product is None:
            current_product = self.rows[0][0]

        current_row = self.rows[current_row_idx]

        # Left path, right path
        left, right = current_row[parent_idx], current_row[parent_idx + 1]
        
        # Traverse down the Pyramid
        for i, path in enumerate([left, right]):
            
            # Appends direction to the current path
            current_path += 'R' if i else 'L'

            # Calculate new product with the current path and update current row
            current_product *= path
            current_row_idx += 1

            # If new product is greater than target, revert changes, 
            # and skip current path
            if current_product > target:
                current_path = current_path[:-1]
                current_product /= path
                current_row_idx -= 1
                continue

            # If target is found and we are at the end of the pyramid,
            # return the path
            elif current_product == target and \
                 current_row_idx == len(self.rows):
                return current_path

            # Continue down the pyramid if there are still rows to traverse
            elif current_row_idx < len(self.rows):
                found = self.findPath(target, parent_idx + i, current_row_idx,
                 current_product, current_path)

                # If path exists, return the path and break out of loop
                if found:
                    return found
            
            # Current path doesn't work, continue
            current_path = current_path[:-1]
            current_product /= path
            current_row_idx -= 1
        
        # No path exists, return empty string
        return ""