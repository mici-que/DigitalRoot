def main(num=None):
    def validator(num=None):
        return (
            "num" in vars()  # param defined
            and isinstance(num, int)  # param is integer
            and 0 <= num  # param is non-negative
        )

    if validator(num):
        digitalsum = 0
        strnum = str(num)
        for char in strnum:
            digitalsum = digitalsum + int(char)
        return digitalsum
    return False
