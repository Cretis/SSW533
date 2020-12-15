import HmdbOperation
import GetData


def save_commit(id, addition, deletion, total, author_id,year,month,day):
    HmdbOperation.add_commit(id, addition, deletion, total, author_id,year,month,day)


def save_request(id, number, state, title, body, locked, assignees, testers, user_id, user_login, user_name,iden):
    if (locked):
        tiny = 1
    else:
        tiny = 0
    HmdbOperation.add_request(id, number, state, title, body, tiny)
    HmdbOperation.add_user(user_id, user_login, user_name,iden)
    for item in assignees:
        HmdbOperation.add_assignees_rela(item['id'], id)
        HmdbOperation.add_user(item['id'],'','','empolyee')
    for item in testers:
        HmdbOperation.add_tester_rela(item['id'], id)
        HmdbOperation.add_user(item['id'],'','','empolyee')

def save_url(url,id):
    HmdbOperation.add_url(url,id)
