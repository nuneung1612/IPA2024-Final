import subprocess

def showrun():
    # read https://www.datacamp.com/tutorial/python-subprocess to learn more about subprocess
    command = ['ansible-playbook', '<!!!REPLACEME with playbook yaml file!!!>']
    result = subprocess.run(command, capture_output=True, text=True)
    result = result.stdout
    if 'ok=2' in result:
        return <!!!REPLACEME!!!>
    else:
        return '<!!!REPLACEME!!!>
