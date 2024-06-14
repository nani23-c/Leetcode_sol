class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            i.reverse()
            for a in range(len(image)):
                if(i[a]==0):
                    i[a]=1
                else:
                    i[a]=0
                
        return image