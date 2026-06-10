from prefect import flow, task
from prefect_github import GitHubCredentials


github_credentials_block = GitHubCredentials(token="my_token")
github_credentials_block.save(name="my-github-credentials-block")

@task
def create_message():
    msg = 'Hello from Task'
    return(msg)

@flow
def something_else():
    result = 10
    return(result)

@flow
def hello_world():
    sub_flow_message = something_else()
    task_message = create_message()
    new_message = task_message + str(sub_flow_message)
    print(new_message)

if __name__ == "main":
    hello_world()