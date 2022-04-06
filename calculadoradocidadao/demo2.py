class Index:
    def uncovered_if(self, var=True):
        if var:
            return False
        else:
            return True

    def fully_covered(self):
        return True

    def uncovered(self):
        return True
