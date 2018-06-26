class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        
        width = min(C, G) - max(A, E)
        height = min(D, H) - max(B, F)
        
        if width <= 0 or height <= 0:
            return (C-A)*(D-B) + (G-E)*(H-F)
        else:
            return (C-A)*(D-B) + (G-E)*(H-F) - height*width
        
        