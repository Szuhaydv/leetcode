def fill(image, sr, sc, start_color, fill_color):
    if sr < 0 or sr >= len(image): return
    if sc < 0 or sc >= len(image[0]): return
    if image[sr][sc] == fill_color: return
    if image[sr][sc] != start_color: return
    image[sr][sc] = fill_color
    fill(image, sr - 1, sc, start_color, fill_color)
    fill(image, sr + 1, sc, start_color, fill_color)
    fill(image, sr, sc - 1, start_color, fill_color)
    fill(image, sr, sc + 1, start_color, fill_color)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        fill(image, sr, sc, image[sr][sc], color)
        return image
