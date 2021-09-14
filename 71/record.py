class RecordScore():
    max_score = float('-inf')

    def __call__(self, score):
        self.max_score = max(self.max_score, score)
        return self.max_score
