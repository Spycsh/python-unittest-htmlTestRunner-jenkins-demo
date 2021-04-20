"""
@author: Spycsh
"""


class Demo:
    @staticmethod
    def insert_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key

        return arr

    @staticmethod
    def insert_sort_wrong(arr):
        for i in range(1, len(arr)):
            j = i - 1
            while j >= 0 and arr[i] < arr[j]:   # ! this arr[i] is overridden in next line so yield wrong result
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = arr[i]

        return arr
