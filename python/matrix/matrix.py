class Matrix:
    def __init__(self, matrix_string):
        self.rows = []
        for string in matrix_string.split("\n"):
            self.rows.append(list(map(int, string.split())))

    def row(self, index):
        return self.rows[index -1]

    def column(self, index):
        return [r[index -1] for r in self.rows]
