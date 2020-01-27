# 替换空格
class Solution:
    def __init__(self):
        pass

    def process(self, sentence):
        if type(sentence) == list:
            count = 0
            length = 0
            for letter in sentence:
                if letter == '#':
                    break
                else:
                    length += 1
                    if letter == ' ':
                        count += 1

            j = length + count * 2 - 1    
            for i in range(length-1, -1, -1):
                if sentence[i] != ' ':
                    sentence[j] = sentence[i]
                else:
                    sentence[j] = '0'
                    j -= 1
                    sentence[j] = '2'
                    j -= 1
                    sentence[j] = '%'
                j -= 1

                if i == j:
                    break

        return sentence
    
if __name__ == '__main__':
    solution = Solution()
    # demo = ['w', 'e', ' ', 'a', 'r', 'e', ' ', 'o', 'n', 'e', ' ', ' ', 'u', 'n', 'i', 'o', 'n', '#', '#', '#', '#', '#', '#', '#', '#', '#']
    demo = [' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
    demo = solution.process(demo)
    
    for letter in demo:
        if letter == '#':
            break
        print(letter, end='')
    print()