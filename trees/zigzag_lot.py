def zigzagLevelOrder(A):
    l_to_r, r_to_l = [A], []
    return_val = []
    while l_to_r or r_to_l:
        level_list = []
        while l_to_r:
            node = l_to_r[0]
            level_list.append(node.val)
            if node.left:
                r_to_l.append(node.left)
            if node.right:
                r_to_l.append(node.right)
            del l_to_r[0]
        return_val.append(level_list)

        level_list = []
        while r_to_l:
            node = r_to_l.pop()
            level_list.append(node.val)
            if node.right:
                l_to_r.insert(0, node.right)
            if node.left:
                l_to_r.insert(0, node.left)
        return_val.append(level_list)

    return return_val
