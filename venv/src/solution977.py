class solution:
    def sortedSquares(self,A):
        lenA = len(A)
        negBound = -1
        for index, num in enumerate(A):
            if num >= 0:
                negBound = index - 1
                break;
        ans = list()
        nonNeg = negBound +1
        while negBound >= 0 or nonNeg < lenA:
            if negBound < 0:
                ans.append(A[nonNeg]*A[nonNeg])
                nonNeg += 1
            elif nonNeg == lenA:
                ans.append(A[negBound]*A[negBound])
                negBound -= 1
            elif A[negBound]*A[negBound] < A[nonNeg]*A[nonNeg]:
                ans.append(A[negBound]*A[negBound])
                negBound -= 1
            else:
                ans.append(A[nonNeg] * A[nonNeg])
                nonNeg += 1
        return ans

    def main(self,A):
        newlist = self.sortedSquares(A)
        print(newlist)
if __name__ == "__main__":
    A = [-5,-4,0,3,4,5]
    objectName = solution()
    objectName.main(A)