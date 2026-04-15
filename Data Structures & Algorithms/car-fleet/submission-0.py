class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        pairs = [(p,s) for p,s in zip(position,speed)]
        pairs.sort(reverse=True)
        for pair in pairs:
            time.append((target-pair[0])/pair[1])
            if len(time)>=2 and time[-1]<=time[-2]:
                time.pop() 
        return len(time)
            
