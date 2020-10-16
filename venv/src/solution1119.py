class solution:
    def removeVowels(self, s: str) -> str:
        news = ''
        for char in s:
            if char == 'a' or char == 'e'or char == 'i'or char == 'o'or char == 'u':
               continue
            news += char
        return news
    def main(self,s: str):
        news = self.removeVowels(s)
        print(news)

if __name__ == "__main__":
    objectName = solution()
    s = "leetcodeisacommunityforcoders"
    objectName.main(s)
