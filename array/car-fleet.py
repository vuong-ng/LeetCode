class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time_passed = 0
        stack = []
        pos_speed = []
        for pos, speed in zip(position, speed):
            pos_speed.append((pos, speed))
        pos_speed.sort()
        stack.append((target - pos_speed[-1][0])/pos_speed[-1][1])
        for i in range(len(pos_speed)-2, -1,-1):
            if (target - pos_speed[i][0])/pos_speed[i][1] > stack[-1]:
                stack.append((target - pos_speed[i][0])/pos_speed[i][1])
        return len(stack)



















        pos_speed = []
        stack = []
        # res = 0
        
        for i,j in zip(position, speed):
            pos_speed.append([i, j])
        pos_speed.sort()
        stack.append((target - pos_speed[-1][0])/pos_speed[-1][1])
        for i in range(len(pos_speed)-2,-1,-1):
            if (target - pos_speed[i][0])/pos_speed[i][1] > stack[-1]:  # car behind has more steps to go -> seperate fleet
                # stack.pop()
                stack.append((target - pos_speed[i][0])/pos_speed[i][1])
                # pos smaller and times larger -> can't be reached -> pop the value before
                # res+=1
                # stack.pop()
                # stack.append((p,s))

        return len(stack)   
                




        
        
        


        














        
        # pairs = [[p, s] for p, s in zip(position, speed)]

        # stack = []
        # for p, s in sorted(pairs)[::-1]:
        #     if not stack:
        #         stack.append((target-p)/s)
        #     if stack and (target - p)/s > stack[-1]:
        #         stack.append((target - p)/s)

        # return len(stack)

        