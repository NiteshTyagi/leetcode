class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        # return [3,4,2,3,2]
        result = []
        def flip_list(arr,s):
            if s==1:
                result.append(arr[0])
                return arr[1:s+1] + arr[0:1] + arr[s+1:]
            else:
                result.append(s)
                return arr[:s][::-1]+arr[s:]
            # print(arr,s,arr[:s][::-1]+arr[s:],sep='<----222---->')
            
        temp = arr.copy()
        temp.sort()
        for k in range(len(temp)-1,-1,-1):
            maximum = temp[k]
            flag = False
            max_index = arr.index(maximum)
            
            if  arr!=temp and max_index!=k and max_index!=0:
                arr = flip_list(arr,max_index+1)
                flag = True
                
            if arr!=temp:
                if flag or max_index==0:
                    result.append(maximum)
                    arr = arr[:maximum][::-1]+arr[maximum:]
            else:
                break
                
        return result
