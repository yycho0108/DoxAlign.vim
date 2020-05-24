#!/usr/bin/env python3
import re


def doxygen_align(arg):
    """
    Format doxygen argument (C++)
    """
    # Determine indentation.
    indent = len(arg) - len(arg.lstrip())

    # Determine content.
    content = ''
    for line in arg.split('\n')[1:-1]:
        m = re.match('^\s*\/?\*+\s*(.*)$', line)
        content += m.group(1) + '\n'

    ppre = '\s*'
    pbrief = '{}(@brief)\s+(.+?(?=@|$|\n\n))'.format(ppre)
    pparam = '{}(@t?param)\s+(\w+)\s+(.+?(?=@|$))'.format(ppre)
    preturn = '{}(@return)\s+(.+?(?=@|$))'.format(ppre)
    pany = '(.+?(?=@|$))'
    pattern = '(?:(?:{})|(?:{})|(?:{})|(?:{}))'.format(
        pbrief, pparam, preturn, pany)
    entries = re.findall(pattern, content, re.S)

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
    print(c0, c1, c2)
    print('==Final==')

    def wrap_with_prefix(prefix, lhs, rhs, maxlen=80):
        out = []
        o = lhs
        if False:
            # Wrap at char boundary
            while rhs:
                d = maxlen - len(o)
                out.append(o + rhs[:d])
                rhs = rhs[d:]
                o = prefix
        else:
            # Wrap at word boundary
            for w in re.finditer('\w+', rhs):
                w = w.group(0)
                if len(o + ' ' + w) <= maxlen:
                    o += ' ' + w
                else:
                    out.append(o)
                    o = prefix
            out.append(o)
        return out

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
            out += (prefix + re.sub('\s+', ' ', entry[7].strip())) + ('\n')
            # Optional: Add additional newline below long description
            out += (prefix + '\n')
    out = ' ' * c0 + '/**\n' + out + ' ' * (c0+1) + '*/'
    return out


def main():
    arg = \
        '''  /**
    * @brief  Function description.
    *
    * Long description .............
    * @tparam X x
    * @param  alpha   loerm ipsum dolor sit amet why do I remember such text and
    * blah blah alpha beta alpha beta alpha beta mega gamma
    * @param  beta     hmm
    * @return The      input pointer `beta` offset by `alpha`. Long ass comment long ass comment
    */ '''

    out = doxygen_align(arg)
    print('<out>')
    print(out)
    print('</out>')


if __name__ == '__main__':
    main()
