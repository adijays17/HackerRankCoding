def divide(dividend: 'int', divisor: 'int') -> 'int':
        if dividend == 0:
            return 0
        flag = False
        if dividend<0:
            dividend = dividend*-1
            flag = not flag
        if divisor<0:
            divisor = divisor*-1
            flag = not flag
        divi = str(dividend)
        out = ''
        temp = 0
        for each in range(len(divi)):
            temp = temp + int(divi[each])
            quo = 0
            if temp >= divisor:
                while temp >= divisor:
                    rem = temp - divisor
                    quo += 1
                    temp = temp - divisor
            else:
                temp = temp*10
                out = out + "0"
                continue
            out = out + str(quo)
            temp = rem*10
        if out == '':
            return 0
        if flag:
            out = int(out)*-1
        if (-2**31) <= int(out) >= (2**31):
            out = int(2**31 - 1)
        return int(out)

print(divide(100,3))