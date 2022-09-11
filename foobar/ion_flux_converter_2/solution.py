import math
def solution(h, q):
    def getHeightOfConverter(node):
        k = math.log(node + 1, 2) 
        if k.is_integer():
            return k
        else:
            # math.floor( math.log(node,2)) alternative
            # convert to binary and count the number digit - 1
            i = int(node).bit_length() - 1
            x = 2**i - 1
            return getHeightOfConverter(node - x)
    
    # 2**h - 1
    def converter_is_left(converter):
        converter_height = getHeightOfConverter(converter)
        parent_height_if_right_child = getHeightOfConverter(converter+1)
        if converter_height + 1 == parent_height_if_right_child:
            return False
        else:
            parent_height_if_left_child = getHeightOfConverter(converter + 2**converter_height)
            if converter_height + 1 == parent_height_if_left_child:
                return True

    def helper(converter,h):
        converter_height = getHeightOfConverter(converter)
        if converter_height >= h:
            return -1
        if converter_is_left(converter):
            converter_label = 2**converter_height + converter
        else:
            converter_label = converter + 1
        return int(converter_label)
    return [ helper(i,h) for i in q]

# print( solution(3, [7, 3, 5, 1]) )
# print( solution(5, [19, 14, 28]) )

