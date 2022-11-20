class ArrayOfIntegers:
    def findPairs(self, array):
        count = 0
        dict = {}
        
        for swi in range(len(array)):
            if len(str(array[swi])) not in dict:
                dict[len(str(array[swi]))] = [array[swi]]
            else:
                dict[len(str(array[swi]))].append(array[swi])

        print(dict)

        for key, values in dict.items():
            if len(values) < 2:
                continue
            else:
                for swi in range(len(values)-1):
                    for swj in range(swi+1, len(values)):
                        diff = 0
                        num1 = str(values[swi])
                        num2 = str(values[swj])

                        if num1 == num2:
                            continue

                        for swk in range(len(str(values[swi]))):
                            if num1[swk] != num2[swk]:
                                diff += 1

                            if diff > 1:
                                break

                        if diff < 2:
                            count += 1

        return count

if __name__ == "__main__":
    obj = ArrayOfIntegers()
    
    array = [1, 151, 241, 1, 9, 22, 351]

    print(obj.findPairs(array))