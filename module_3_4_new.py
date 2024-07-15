def single_root_words(root_word, *other_words):
    same_words = []
    # print(root_word)
    # print(other_words)
    # print(other_words[0][0])
    root = root_searcher(root_word)
    #same_words.append(root_word)
    #print(other_words)
    for word in other_words:
        if str(word).__contains__(root):
            same_words.append(str(word))
    return same_words
def root_searcher(word_in):
    word_in = word_in.lower()
    prefixes = ['un', 'im', 'in', 'il', 'ir', 'dis', 'mis', 'anti', 'auto', 'pre', 'mid', 'post', 'super', 'micro']
    postfixes = ['er', 'or', 'ian', 'an', 'ist', 'ant', 'ment', 'ent', 'ee', 'ess', 'ity', 'ance', 'ence', 'ancy', 'ency', \
                 'ism', 'hood', 'ure', 'tion', 'sion', 'ion', 'dom', 'ness', 'ship', 'th']
    for prefix in prefixes:
        if prefix == word_in[0:len(prefix)]:
            root = word_in[len(prefix):]
            break
        else:
            root = word_in
    for postfix in postfixes:
        if postfix == root[len(root) - len(postfix):len(root)]:
            root = root[0:len(root) - len(postfix)]
    #print(root)
    return root

if __name__ == '__main__':
    # print('ОДНОКОРЕННЫЕ. Поиск однокоренных английских существительных в единственном числе.')
    #
    # list_in = [str(value) for value in input('Введите список слов, разделенных пробелами: ').split()]
    # cognates_words(list_in[0], list_in[1:])

    result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
    result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
    print(result1)
    print(result2)