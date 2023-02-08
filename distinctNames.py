from collections import defaultdict


class Solution:
    def distinctNames(self, ideas):
        # result = 0
        # for swi in range(len(ideas)):
        #     for swj in range(len(ideas)):
        #         if swi == swj or ideas[swi][0] == ideas[swj][0]:
        #             continue
        #         idea_a, idea_b = ideas[swi], ideas[swj]
        #         idea_a = list(idea_a)
        #         idea_b = list(idea_b)
        #         idea_a[0], idea_b[0] = idea_b[0], idea_a[0]
        #         idea_a = "".join(idea_a)
        #         idea_b = "".join(idea_b)

        #         if idea_a not in ideas and idea_b not in ideas:
        #             # print(f'Name: {idea_a} {idea_b}')
        #             result += 1

        # return result

        result = 0

        dict = defaultdict(list)

        for swi in range(len(ideas)):
            # print(f'For idea: {ideas[swi]} and dict: {dict}')
            if ideas[swi][0] not in dict:
                dict[ideas[swi][0]] = []

            dict[ideas[swi][0]].append(ideas[swi])

        # print(f'dict: {dict}')

        simplified_dict = []

        for key, values in dict.items():
            simplified_dict.append(len(values))

        major = 1

        for num in simplified_dict:
            major = major * num

        for swi in range(len(simplified_dict)-1):
            for swj in range(len(simplified_dict)):
                if swi == swj:
                    continue

                result = result + (simplified_dict[swi] * simplified_dict[swj])

        # print(f'simplified_dict: {simplified_dict}')

        return result

if __name__ == "__main__":
    obj = Solution()

    print(obj.distinctNames(ideas = ["coffee","donuts","time","toffee"]) == 6)
    print(obj.distinctNames(ideas = ["lack","back"]) == 0)