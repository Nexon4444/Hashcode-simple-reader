import re

class Reader:
    def __init__(self, path):
        self.path = path
        self.first_line = list()
        self.other_lines = list()
        self.tag_dict = dict()

    def read(self):
        with open(self.path, "r+", encoding="utf-8") as f:
            for indx, line in enumerate(f):
                if indx == 0:
                    regex = r"(\d+)"
                    # other_lines = f.readlines()
                    matches = re.finditer(regex, line.strip(), re.MULTILINE)
                    for matchNum, match in enumerate(matches, start=1):
                        # print(str(match.g))
                        self.first_line.append(int(match.group(1)))
                else:
                    regex = r"(\S+)"
                    matches = re.finditer(regex, line.strip(), re.MULTILINE)

                    pom = list()
                    for matchNum, match in enumerate(matches, start=1):
                        for groupNum in range(0, len(match.groups())):
                            groupNum = groupNum + 1
                            pom.append(match.group(groupNum))
                    self.other_lines.append(pom)
                    # for id in range(2, len(pom)):
                    #     self.tag_dict[pom[id]].setdefault([], len(self.other_lines)).append(len(self.other_lines))


            # print(self.first_line)
            # print(self.other_lines)

# r = Reader("a_example.txt")
# r.read()