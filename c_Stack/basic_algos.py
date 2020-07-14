# utf-8
"""
    1) 数制转换
    2) 括号匹配的校验
    3) 行编辑程序
    4) 迷宫求解
    5) 表达式求值
    6) a simple browser
"""

import sys

from c_Stack.stacks import LinkedStack

sys.path.append('stacks.py')


def number_base_conversion(input_number: int, base=8):
    stack = LinkedStack()
    while input_number:
        input_number, r = divmod(input_number, base)
        stack.push(r)

    out_put_lis = []
    data = stack.pop()
    while data is not None:
        out_put_lis.append(str(data))
        data = stack.pop()
    return ''.join(out_put_lis)


def brackets_matching_check(input_brackets: str):
    """核心: 期待的紧迫程度，利用栈"""
    def pair_brackets(a: str, b: str):
        return True if a + b in ['()', '[]'] else False
    left_bracket_lis = ['(', '[']
    right_bracket_lis = [')', ']']
    stack = LinkedStack()
    for bracket in input_brackets:
        if bracket not in left_bracket_lis + right_bracket_lis:
            return "invalid input"
        if bracket in left_bracket_lis:
            stack.push(bracket)
        elif bracket in right_bracket_lis:
            bracket_to_pair = stack.pop()
            if not pair_brackets(bracket_to_pair, bracket):
                return False
    if stack.pop():
        return False
    else:
        return True


def line_editor():
    """
    这个输入缓冲区为一个stack，每当从终端接受一个字符之后，
    判断：
        如果它既不是退格符(#)也不是退行符(@),则将该字符压入栈顶；
        如果它是一个退格符(#)stack出栈一个字符；
        如果它是一个退行符(@)清空stack；
    :return:
    """
    codes = []
    s = input()
    stack = LinkedStack()
    while s:
        if s == 'EOF':
            return '\n'.join(codes)
        for char in s:
            if char in ['#', '@']:
                if char == '#':
                    stack.pop()
                else:
                    while not stack.is_empty():
                        stack.pop()
            else:
                stack.push(char)
        line_code = []
        while not stack.is_empty():
            line_code.insert(0, stack.pop())
        codes.append(''.join(line_code))

        s = input()
    return '\n'.join(codes)


class Browser:
    """
        a simple browser realize
        解答：我们使用两个栈，X 和 Y，我们把首次浏览的页面依次压入栈 X，当点击后退按钮时，再依次从栈 X 中出栈，
        并将出栈的数据依次放入栈 Y。当我们点击前进按钮时，我们依次从栈 Y 中取出数据，放入栈 X 中。
        当栈 X 中没有数据时，那就说明没有页面可以继续后退浏览了。当栈 Y 中没有数据，
        那就说明没有页面可以点击前进按钮浏览了。
    """
    def __init__(self):
        self.forward_stack = LinkedStack()
        self.back_stack = LinkedStack()

    def can_forward(self):
        if self.back_stack.is_empty():
            return False

        return True

    def can_back(self):
        if self.forward_stack.is_empty():
            return False

        return True

    def open(self, url):
        print("Open new url %s" % url, end="\n")
        self.forward_stack.push(url)

    def back(self):
        if self.forward_stack.is_empty():
            return

        top = self.forward_stack.pop()
        self.back_stack.push(top)
        print("back to %s" % top, end="\n")

    def forward(self):
        if self.back_stack.is_empty():
            return

        top = self.back_stack.pop()
        self.forward_stack.push(top)
        print("forward to %s" % top, end="\n")


if __name__ == '__main__':
    print('test 1 *********************************************')
    print(number_base_conversion(1348))

    print('test 2 *********************************************')
    print(brackets_matching_check('[([][])]'))
    print(brackets_matching_check('[([][]())]()'))
    print(brackets_matching_check('[([][]())'))
    print(brackets_matching_check('[(])'))

    print('test 6 *********************************************')
    browser = Browser()
    browser.open('a')
    browser.open('b')
    browser.open('c')
    if browser.can_back():
        browser.back()

    if browser.can_forward():
        browser.forward()

    browser.back()
    browser.back()
    browser.back()