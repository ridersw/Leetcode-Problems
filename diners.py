class Solution:
    def diners(self, N, K, M, S):
        count = 0

        # for swi in range(len(S)):
        #     for swj in range(S[swi], S[swi] + K+1):
        #         if swj not in S:
        #             S.append(swj)

        #     for swj in range(S[swi], S[swi] - K - 1, -1):
        #         if swj not in S:
        #             S.append(swj)

        # S.sort()

        # print(f'S: {S}')

        # arr = [0] * (N+1)

        # for swi in range(len(arr)):
        #     if swi in S:
        #         arr[swi] = 1

        # print(f'arr: {arr}')

        # for swi in range(0, N+1):
        #     if swi < K:
        #         # print(f'Found: swi < K and sum(S[swi:swi+K]): {sum(arr[swi:swi+K])}')
        #         if sum(arr[swi:swi+K]) + sum(arr[:swi])== 0:
        #             count += 1
        #             arr[swi] = 1
        #     elif swi+K > N:
        #         if sum(arr[swi-K:swi]) == 0:
        #             count += 1
        #             arr[swi] = 1
        #     else:
        #         if sum(arr[swi:swi+K]) + sum(arr[swi-K:swi]) == 0:
        #             count += 1
        #             arr[swi] = 1

        # print(f'arr: {arr}')

        # return count

        seating = [0] * (N+1)
        
        for num in S:
            seating[num-1] = 1

        print(f'seating: {seating}')

        for swi in range(0, N):
            if swi < K:
                # print(f'Found: swi < K and sum(S[swi:swi+K]): {sum(arr[swi:swi+K])}')
                if sum(seating[swi:swi+K]) + sum(seating[:swi])== 0:
                    count += 1
                    seating[swi] = 1
            elif swi+K > N:
                if sum(seating[swi-K:swi]) == 0:
                    count += 1
                    seating[swi] = 1
            else:
                if sum(seating[swi:swi+K]) + sum(seating[swi-K:swi]) == 0:
                    count += 1
                    seating[swi] = 1

        print(f'arr: {seating}')

        # for swi in range(len(S)):
        #     for swj in range(S[swi], S[swi] + K+1):
        #         if swj not in S:
        #             S.append(swj)

        #     for swj in range(S[swi], S[swi] - K - 1, -1):
        #         if swj not in S:
        #             S.append(swj)

        return count



if __name__ == "__main__":
    obj = Solution()

    N = 10
    K = 1
    M = 2
    S = [2, 6]

    # N = 15
    # K = 2
    # M = 3
    # S = [11, 6, 14]

    # N = 25
    # K = 2
    # M = 2
    # S = [0, 3]



    print(obj.diners(N, K, M, S))






#N = 10 # total seats
#K = no of seasts to left and right
#M = no of diners seating at table
#S = locations of already seated diners