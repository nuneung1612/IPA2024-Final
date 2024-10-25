import json
import requests
requests.packages.urllib3.disable_warnings()

# Router IP Address is 10.0.15.182
api_url = "https://10.0.15.182/restconf/data"

# the RESTCONF HTTP headers, including the Accept and Content-Type
# Two YANG data formats (JSON and XML) work with RESTCONF 
headers = { "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
           }
basicauth = ("admin", "cisco")
studentID = "65070131"
def create():
    check_url = api_url + "/ietf-interfaces:interfaces/interface=Loopback65070131"
    check_resp = requests.get(
        check_url, 
        auth=basicauth,
        headers=headers,
        verify=False
    )
    if check_resp.status_code == 200:
        return "Cannot create: Interface loopback 65070131"
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback65070131",
            "description": "My RESTCONF loopback",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": "172.30.131.1",
                        "netmask": "255.255.255.0"
                    }
                ]
            },
            "ietf-ip:ipv6": {}
        }
    }


    resp = requests.put(
        # <!!!REPLACEME with URL!!!>,
        api_url + "/ietf-interfaces:interfaces/interface=Loopback65070131",
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 65070131 is created successfully"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))


def delete():
    check_url = api_url + "/ietf-interfaces:interfaces/interface=Loopback65070131"
    check_resp = requests.get(
        check_url, 
        auth=basicauth,
        headers=headers,
        verify=False
    )
    if check_resp.status_code >= 400:
        return "Cannot delete: Interface loopback 65070131"
    

    resp = requests.delete(
        check_url,
        auth=basicauth, 
        headers=headers, 
        verify=False
        )
    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 65070131 is deleted successfully"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))


def enable():
    yangConfig = <!!!REPLACEME with YANG data!!!>

    resp = requests.<!!!REPLACEME with the proper HTTP Method!!!>(
        <!!!REPLACEME with URL!!!>, 
        data=json.dumps(<!!!REPLACEME with yangConfig!!!>), 
        auth=basicauth, 
        headers=<!!!REPLACEME with HTTP Header!!!>, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "<!!!REPLACEME with proper message!!!>"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))


def disable():
    yangConfig = <!!!REPLACEME with YANG data!!!>

    resp = requests.<!!!REPLACEME with the proper HTTP Method!!!>(
        <!!!REPLACEME with URL!!!>, 
        data=json.dumps(<!!!REPLACEME with yangConfig!!!>), 
        auth=basicauth, 
        headers=<!!!REPLACEME with HTTP Header!!!>, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "<!!!REPLACEME with proper message!!!>"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))


def status():
    api_url_status = "<!!!REPLACEME with URL of RESTCONF Operational API!!!>"

    resp = requests.<!!!REPLACEME with the proper HTTP Method!!!>(
        <!!!REPLACEME with URL!!!>, 
        auth=basicauth, 
        headers=<!!!REPLACEME with HTTP Header!!!>, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        response_json = resp.json()
        admin_status = <!!!REPLACEME!!!>
        oper_status = <!!!REPLACEME!!!>
        if admin_status == 'up' and oper_status == 'up':
            return "<!!!REPLACEME with proper message!!!>"
        elif admin_status == 'down' and oper_status == 'down':
            return "<!!!REPLACEME with proper message!!!>"
    elif(resp.status_code == 404):
        print("STATUS NOT FOUND: {}".format(resp.status_code))
        return "<!!!REPLACEME with proper message!!!>"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
