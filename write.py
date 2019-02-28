class writer:
    def __init__(self, list_of_lists):
        self.to_write = list_of_lists

    def write(self):
        with open("result.txt", "w+", encoding="utf-8") as f:
            for l in self.to_write:
                for el in l:
                    f.write(str(el) + " ")
                f.write("\n")

        print("written")
        # print(str())

w = writer([['a', 'l', 'a'], ['m', 'a']])
w.write()