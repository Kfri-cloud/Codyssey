def get_number(prompt, minmun, maxmum):
    while True:
        try:
            number = int(input(prompt))
            if number <= minmun or number >= maxmum:
                print("유효하지 않은 입력입니다. 범위를 벗어났습니다.")
            else:
                return number
        except ValueError:
            print("유효하지 않은 입력입니다. 숫자를 입력해주세요.")