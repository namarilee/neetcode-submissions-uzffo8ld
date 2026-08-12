class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.timemap.get(key, []) #if not found, will return []
        l, r = 0, len(values) - 1
        result = ""

        while l <= r:
            m = (l + r) // 2

            if values[m][1] <= timestamp:
                result = values[m][0]
                l = m + 1
            else:
                r = m - 1

        return result
