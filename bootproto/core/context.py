from bootproto.core.navbar import navbar

list = [1,2,3,4,5]
test_list = [1,2,3,4,list]

context_dict = {
    'navbar': navbar,
    'test_list': test_list
}