def main(num=None):
    def validator(num=None):
        return (
            "num" in vars()  # param defined
            and isinstance(num, int)  # param is integer
            and 0 <= num  # param is non-negative
        )

    def digitalsum(num):
        summa = 0
        while num > 0:
            summa = summa + num % 10
            num = num // 10
        return summa

    def recursivedigitalsum(num):
        while num > 9:
            num = digitalsum(num)
        return num

    if validator(num):
        return recursivedigitalsum(num)
    return False
