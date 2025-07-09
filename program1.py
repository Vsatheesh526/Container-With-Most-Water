class Solution:
    def maxArea(self, walls: List[int]) -> int:
        start, end = 0, len(walls) - 1
        max_water = 0

        while start < end:
            min_height = min(walls[start], walls[end])
            width = end - start
            current_area = min_height * width
            max_water = max(max_water, current_area)

            if walls[start] < walls[end]:
                start += 1
            else:
                end -= 1

        return max_water
