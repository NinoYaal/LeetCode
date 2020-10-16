class solution:
    def toLowerCase(self, s):
        if not s:
            return s
        newstrlist = []
        for char in list(s):
            newchar = ord(char) | 32
            newstrlist.append(chr(newchar))
        return  newstrlist

    def main(self,s):
        print(self.toLowerCase(s))


if __name__ == "__main__":
    objectName = solution()
    s = 'hELlo'
    objectName.main(s)
