class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def timetaken(position, speed):
            time = (target - position) / speed
            if time in fleets:
                return
            elif fleets and max(fleets) > time:
                return
            fleets.append(time)
            return
        fleets = []
        stack = []
        for pos, spd in zip(position, speed):
            stack.append((pos,spd))
        stack = sorted(stack, key = lambda x: x[0], reverse=True)
        for each in stack:
            timetaken(each[0], each[1])
        return len(fleets)