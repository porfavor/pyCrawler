class Utils:
    def __init__(self):
        print 'Init class'

    def pick(self, total_list, num):
        i = 0;
        while True:
            element = total_list[i]

            i += 1
            if i == num:
                break
