class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        subseq=10
        right=subseq-1
        res=set()
        res_hash={}
        while right<len(s):
            left=right-subseq+1
            substr=s[left:right+1]
            if res_hash.get(substr):
                res.add(substr)
            else:
                res_hash[substr]=1
            right+=1
        return list(res)
        