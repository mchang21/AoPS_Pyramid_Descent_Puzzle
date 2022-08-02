class Pyramid:
    def __init__(self, rows):
        self.rows = rows

    def findPath(self, target, parent_idx = 0, current_row_idx=1,
     current_product=None, current_path = ""):

        # Sets the initial product to be the number at the top of the pyramid
        if current_product is None:
            current_product = self.rows[0][0]

        current_row = self.rows[current_row_idx]

        # Left path, right path
        # parentIdx is of previous row
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