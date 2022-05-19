class Solution:
    def myAtoi(self, s: str) -> int:

        state = ["w", "s", "d", "n"]

        sign_set = ['+', '-']
        sign = '+'

        curr_state = ""

        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)

        res = []

        n = len(s)

        for i in range(n):

            if (i == 0):

                if (s[i] == " "):
                    curr_state = state[0]
                elif (s[i] in sign_set):
                    curr_state = state[1]
                    sign = s[i]
                elif (s[i].isdigit()):
                    curr_state = state[2]
                    res.append(s[i])
                else:
                    curr_state = state[3]

            else:

                if (curr_state == state[0]):

                    if (s[i] == " "):
                        continue
                    elif (s[i] in sign_set):
                        curr_state = state[1]
                        sign = s[i]
                    elif (s[i].isdigit()):
                        curr_state = state[2]
                        res.append(s[i])
                    else:
                        curr_state = state[3]

                else:

                    if (s[i].isdigit()):
                        curr_state = state[2]
                        res.append(s[i])
                    else:
                        curr_state = state[3]

            if curr_state == state[3]:
                break

        if (len(res) == 0):
            return 0

        res_int = 0

        for j in range(len(res)):

            if ((res_int > int(INT_MAX / 10)) or (res_int == int(INT_MAX / 10) and int(res[j]) >= 7)):
                res_int = INT_MAX
                break
            elif (res_int < int(INT_MIN / 10) or (res_int == int(INT_MIN / 10) and int(res[j]) >= 8)):
                res_int = INT_MIN
                break

            if (sign == '-'):

                res_int = res_int * 10 - int(res[j])

            else:

                res_int = res_int * 10 + int(res[j])

        return (res_int)