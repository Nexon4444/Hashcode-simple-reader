from reader import Reader
class Solve:
    def __init__(self, file):
        print("starting solver")
        self.file = file
        r = Reader(file)
        r.read()
        # horizontals =
        vertices = self.translate_to_vertices(r.other_lines)
        slides = self.create_slides(vertices)
        # print("slide1: " + str(slides[2].slide_tags))
        # print("slide2: " + str(slides[1].slide_tags))
        # print("interesect: " + str(slides[2].calc_value(slides[1])))
        # print(str(vertices))

        # verticals =
        verticals =
        print("generating graph")
        graph = dict()
        for indx, slide in enumerate(slides):
            graph[slide] = {s: slide.calc_value(s) for indx2, s in enumerate(slides) if (indx != indx2)}
        print("graph generated")
        print(str(graph))

    def translate_to_vertices(self, list):
        return [Picture(l, id) for id, l in enumerate(list)]

    def translate_to_verticals(self, list):
        return [for

    def create_slides(self, vertices):
        return [Slide(v) for v in vertices]


class Picture:
    def __init__(self, list, id):
        self.id = id
        self.ust = list[0]
        self.n_tags = int(list[1])
        self.tags = [list[n] for n in range(2, len(list))]

class Slide:
    def __init__(self, pic1, pic2=None):
        self.pics = list().append(pic1)
        self.slide_tags = pic1.tags
        self.slide_n = pic1.n_tags
        if pic2 is not None:
            self.pics.append(pic2)
            self.slide_tags.append(pic2.tags)
            self.slide_n += pic2.n_tags
        self.last_calc = 0 #niebezpieczne

    def calc_value(self, slide):
        self.last_calc = min([slide.slide_n, self.slide_n, self.count_union(slide)])
        return self.last_calc

    def count_union(self, slide):
        # to_ret = len(set(self.slide_tags).intersection(slide.slide_tags))
        return len(set(self.slide_tags).intersection(slide.slide_tags))

# class Graph:

Solve("e_shiny_selfies.txt")




