from prefect import flow, task
#from prefect.blocks.system import String

#string_blocks = String.load("future-nba-champs")

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