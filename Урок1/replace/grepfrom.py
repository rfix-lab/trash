#fileList = os.listdir(path)
path='/home/local/TENSOR-CORP/rs.silin/Документы/Python/Урок1/replace/'
with open (path'group.txt', 'r') as f:
    for word in f:
        try:
            int(word)
        except ValueError:
            print('pass')
        else:
            with open ('/home/local/TENSOR-CORP/rs.silin/Документы/Python/Урок1/replace/group_out', 'w') as f:
                print(word)