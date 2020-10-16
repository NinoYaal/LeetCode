class solution:
    def runningSum(self, nums):
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return  nums
    def main(self, nums):
        print(self.runningSum(nums))
        return

if __name__ == "__main__":
    objectName = solution()
    nums = [1,2,3,4]
    objectName.main(nums)
