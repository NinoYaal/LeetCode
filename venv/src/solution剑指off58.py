class solution:
    def reverseLeftWords(self, s, n):
        news1 = s[n:]
        news2 = s[:n]
        news = news1 + news2
        return news
    def main(self,s,n):
        news = self.reverseLeftWords(s,n)
        print(news)

if __name__ == "__main__":
    objectName = solution()
    s = "cdefgab"
    objectName.main(s, 2)
