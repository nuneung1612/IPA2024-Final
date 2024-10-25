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
    check_url = api_url + "/ietf-interfaces:interfaces/interface=Loopback65070131"
    check_resp = requests.get(
        check_url, 
        auth=basicauth,
        headers=headers,
        verify=False
    )
    if check_resp.status_code >= 400:
        return "Cannot enable: Interface loopback 65070131"
    
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback65070131",
            "description": "Enable Configured by RESTCONF",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
        }
    }

    resp = requests.put(
        check_url, 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 65070131 is enabled successfully"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))



def disable():    
    check_url = api_url + "/ietf-interfaces:interfaces/interface=Loopback65070131"
    check_resp = requests.get(
        check_url, 
        auth=basicauth,
        headers=headers,
        verify=False
    )
    if check_resp.status_code >= 400:
        return "Cannot shutdown: Interface loopback 65070131"
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback65070131",
            "description": "Disable Configured by RESTCONF",
            "type": "iana-if-type:softwareLoopback",
            "enabled": False,
        }
    }

    resp = requests.put(
        check_url, 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 65070131 is shutdown successfully"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))

def status():    
    api_url_status = api_url+"/openconfig-interfaces:interfaces/interface=Loopback65070131/state"
    resp = requests.get(
        api_url_status, 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        response_json = resp.json()
        admin_status = response_json["openconfig-interfaces:state"]["admin-status"]
        oper_status = response_json["openconfig-interfaces:state"]["oper-status"]
        print("admin: ", admin_status, "oper: ", oper_status)
        if admin_status == 'UP' and oper_status == 'UP':
            return "Interface loopback 65070131 is enabled"
        elif admin_status == 'DOWN' and oper_status == 'DOWN':
            return "Interface loopback 65070131 is disabled"
    elif(resp.status_code == 404):
        print("STATUS NOT FOUND: {}".format(resp.status_code))
        return "No Interface loopback 65070131"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))