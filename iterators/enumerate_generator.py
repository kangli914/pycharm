
def enumerate(data):
    """generator version - Gnerator is another way of creating iterators. __It uses a function rather than a separate class__"""

    for index in range(len(data)):
        t =  (index, data[index])
        # print(f"returned {t}")
        yield t


if __name__ == "__main__":
    g = enumerate("abcde")
    for item in g:
        print(item)