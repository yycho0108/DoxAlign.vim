#!/usr/bin/env python3

import re
import textwrap


def doxygen_align(arg):
    """
    Format doxygen argument (C++)
    """
    # Determine indentation.
    indent = len(arg) - len(arg.lstrip())

    # Determine content.
    content = ''
    for line in arg.strip().split('\n')[1:-1]:
        m = re.match('^\s*\/?\*+\s*(.*)$', line)
        content += m.group(1) + '\n'

    # Configure regex patterns.
    # Not the best regex but gets the job done for now.
    ppre = '\s*'
    pbrief = '{}(@brief)\s+(.+?(?=@|$|\n\n))'.format(ppre)
    pparam = '{}(@t?param(?:\[(?:in|out|in,\s*out)?\])?)\s+(\w+)\s+(.+?(?=@|$))'.format(ppre)
    preturn = '{}(@return)\s+(.+?(?=@|$))'.format(ppre)
    pany = '(.+?(?=@|$))'
    pattern = '(?:(?:{})|(?:{})|(?:{})|(?:{}))'.format(
        pbrief, pparam, preturn, pany)
    entries = re.findall(pattern, content, re.S)

    # Determine indentations.
    # FIXME(yycho0108): There's probably a better way to do this.
    c0 = indent  # size of cell 0, indentation
    c1 = 0
    c2 = 0
    for entry in entries:
        if entry[0]:
            # brief
            c1 = max(c1, len(entry[0]))
        elif entry[2]:
            # param
            c1 = max(c1, len(entry[2]))
            c2 = max(c2, len(entry[3]))
        elif entry[5]:
            # return
            c1 = max(c1, len(entry[5]))
        elif entry[7]:
            # long
            pass

    def wrap_with_prefix(prefix, lhs, rhs, maxlen=80):
        out = []
        rr = textwrap.wrap(rhs, maxlen - len(prefix))
        out.append(lhs + rr[0])
        for r in rr[1:]:
            out.append(prefix + r)
        return out

    # Build output.
    out = ''
    prefix = ' '.ljust(c0+1) + '* '
    for entry in entries:
        if entry[0]:
            # brief
            lhs = prefix + entry[0].ljust(c1+1, ' ')
            rhs = re.sub('\s+', ' ', entry[1])
            for row in wrap_with_prefix(
                    prefix + ' '.ljust(c1+1, ' '), lhs, rhs):
                out += row + '\n'
            out += (prefix + '\n')
        elif entry[2]:
            # param
            lhs = prefix + entry[2].ljust(c1+1, ' ') + \
                entry[3].ljust(c2+1, ' ')
            rhs = re.sub('\s+', ' ', entry[4])
            for row in wrap_with_prefix(
                    prefix + ' '.ljust(c1+1+c2+1, ' '), lhs, rhs):
                out += row + '\n'
        elif entry[5]:
            # return
            lhs = prefix + entry[5].ljust(c1+1, ' ') + ''.ljust(c2+1, ' ')
            rhs = re.sub('\s+', ' ', entry[6])
            # Optional: Add additional newline before return
            out += (prefix + '\n')
            for row in wrap_with_prefix(
                    prefix + ''.ljust(c1+1, ' ') + ''.ljust(c2+1, ' '), lhs, rhs):
                out += row + '\n'
        elif entry[7].strip():
            # long
            lhs = prefix
            rhs = re.sub('\s+', ' ', entry[7].strip())
            for row in wrap_with_prefix(
                    prefix, lhs, rhs):
                out += row + '\n'
            # Optional: Add additional newline below long description
            out += (prefix + '\n')
    out = ' ' * c0 + '/**\n' + out + ' ' * (c0+1) + '*/'
    return out


def main():
    arg = open('sample.txt').read()
    out = doxygen_align(arg)

    print('<in>')
    print(arg)
    print('</in>')

    print('<out>')
    print(out)
    print('</out>')


if __name__ == '__main__':
    main()
