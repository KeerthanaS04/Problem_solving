class Solution:
    def minimumBoxes(self, n: int) -> int:
        # find the maximum height of complete pyramid we can build
        total_boxes = 0
        height = 1

        # keep adding complete layers while we have enough layers
        while total_boxes+height*(height+1)//2<=n:
            total_boxes+=height*(height+1)//2
            height+=1
        
        height-=1
        # calculate the number of ground boxes
        ground_boxes = height*(height+1)//2
        # add remaining boxes one column at a time
        column_height = 1
        while total_boxes<n:
            ground_boxes+=1
            total_boxes+=column_height
            column_height+=1
        return ground_boxes