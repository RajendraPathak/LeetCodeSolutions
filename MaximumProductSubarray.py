class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        final = max(nums)
        nmax, nmin = 1, 1
        for n in nums:
            temp = n*nmax
            nmax = max(n*nmax, n*nmin, n)
            nmin = min(temp, n*nmin, n)
            if final<nmax:
                final= nmax
            # final = max(nmax,final)
        return  final