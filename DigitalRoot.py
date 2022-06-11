def main(num=None):
    def validator(num=None):
        return (
            "num" in vars()  # param defined
            and isinstance(num, int)  # param is integer
            and 0 <= num  # param is non-negative
        )

    def digitalsum(num):
        digitalsum = 0
        while num > 0:
            digitalsum = digitalsum + num % 10
            num = num // 10
        return digitalsum

    if validator(num):
        return digitalsum(num)
    return False
