import requests
import json
import SaveData
import random
import HmdbOperation


def get_repos():
    repo_url = 'https://gitee.com/api/v5/orgs/openharmony/repos'
    page = 1
    repo_params = {"per_page": 100, "page": page}
    repo_res = requests.get(url=repo_url, params=repo_params)
    repo_res = json.loads(repo_res.text)
    lens = len(repo_res)
    while lens == 100:
        page += 1
        repo_params["page"] = page
        new_repo_res = requests.get(url=repo_url, params=repo_params)
        new_repo_res = json.loads(new_repo_res.text)
        repo_res += new_repo_res
        lens = len(new_repo_res)
    return repo_res


def get_pulls(repo_res):
    for repo in repo_res:
        repo_name = repo['name']
        print(repo_name)
        url = 'https://gitee.com/api/v5/repos/openharmony/' + repo_name + '/pulls'
        page = 1
        params = {"access_token": "8ca1da03a355df2fa055647553cfe447", "state": "all", "pre_page": 100, "page": page}
        repo_logs = requests.get(url=url, params=params)
        repo_logs = json.loads(repo_logs.text)
        lens = len(repo_logs)
        while lens == 100:
            page += 1
            params["page"] = page
            new_repo_logs = requests.get(url=url, params=params)
            new_repo_logs = json.loads(new_repo_logs.text)
            repo_logs += new_repo_logs
            lens = len(new_repo_logs)
        for repo_log in repo_logs:
            request_id = repo_log['id']
            number = repo_log['number']
            state = repo_log['state']
            title = repo_log['title']
            body = repo_log['body']
            locked = repo_log['locked']
            assignees = repo_log['assignees']
            testers = repo_log['testers']
            user_id = repo_log['user']['id']
            user_name = repo_log['user']['name']
            user_login = repo_log['user']['login']
            iden = ''
            if 'labels' in repo_log.keys() and len(repo_log['labels']) > 0:
                if repo_log['labels'][-1]['id'] == 82794774 or repo_log['labels'][-1]['id'] == 82794745:
                    iden = 'empolyee'
                else:
                    iden = 'volunteer'
            SaveData.save_request(request_id, number, state, title, body, locked, assignees, testers, user_id,
                                  user_name, user_login, iden)


def get_commits(repo_res):
    for repo in repo_res:
        repo_name = repo['name']
        print(repo_name)
        url = 'https://gitee.com/api/v5/repos/openharmony/' + repo_name + '/commits'
        page = 1
        params = {"access_token": "8ca1da03a355df2fa055647553cfe447", "pre_page": 100, "page": page}
        repo_logs = requests.get(url=url, params=params)
        repo_logs = json.loads(repo_logs.text)
        lens = len(repo_logs)
        while lens == 100:
            page += 1
            params["page"] = page
            new_repo_logs = requests.get(url=url, params=params)
            new_repo_logs = json.loads(new_repo_logs.text)
            repo_logs += new_repo_logs
            lens = len(new_repo_logs)
        for repo_log in repo_logs:
            if repo_log['author'] is not None:
                commit_id = repo_log['stats']['id']
                addition = repo_log['stats']['additions']
                deletion = repo_log['stats']['deletions']
                total = repo_log['stats']['total']
                author_id = repo_log['author']['id']
                author_date = repo_log['commit']['author']['date']
                year = author_date[0:4]
                month = author_date[5:7]
                day = author_date[8:10]
                url = repo_log['html_url']
                SaveData.save_commit(commit_id, addition, deletion, total, author_id, year, month, day)
                SaveData.save_url(url, commit_id)
            else:
                commit_id = repo_log['stats']['id']
                addition = repo_log['stats']['additions']
                deletion = repo_log['stats']['deletions']
                total = repo_log['stats']['total']
                author_id = random.randint(9999999, 99999999)
                author_date = repo_log['commit']['author']['date']
                year = author_date[0:4]
                month = author_date[5:7]
                day = author_date[8:10]
                url = repo_log['html_url']
                SaveData.save_commit(commit_id, addition, deletion, total, author_id, year, month, day)
                SaveData.save_url(url, commit_id)
                if 'huawei' in repo_log['commit']['author']['email']:
                    HmdbOperation.add_user(author_id, '', '', 'empolyee')
                else:
                    HmdbOperation.add_user(author_id, '', '', 'volunteer')


if __name__ == '__main__':
    get_commits(get_repos())
