def polind(polindrom):
    if polindrom==polindrom[::-1]:
        print('True')
    if polindrom!=polindrom[::-1]:
        print('False')

polind('helleh')
polind('dwdwdfe')