from netmiko import ConnectHandler
from pprint import pprint

device_ip = "10.0.15.182"
username = "admin"
password = "cisco"

device_params = {
    "device_type": "cisco_ios",
    "ip": device_ip,
    "username": username,
    "password": password,
}


def gigabit_status():
    ans = ""
    with ConnectHandler(**device_params) as ssh:
        up = 0
        down = 0
        admin_down = 0
        result = ssh.send_command("show ip int br", use_textfsm=True)
        for status in result:
            if status["interface"][0] == "G":
                interface_name = status["interface"]
                st = status["status"]
                ans += str(interface_name)+' '+str(st) +', '
                if status['status'] == "up":
                    up += 1
                elif status['status'] == "down":
                    down += 1
                elif status['status'] == "administratively down":
                    admin_down += 1
        up = str(up)
        down = str(down)
        admin_down=str(admin_down)
        ans += "-->"+up+" up, "+down +" down, "+ admin_down +" administratively down"
        pprint(ans)
        return ans
