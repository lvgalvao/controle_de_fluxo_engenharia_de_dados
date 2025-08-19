class MeuComparavel:
    def __init__(self, val: int):
        self.val = val

    def __eq__(self, other:int) -> bool:
        print('Sou igual?')
        return self.val == other


if __name__ == "__main__":
    print(MeuComparavel(1) == 1)