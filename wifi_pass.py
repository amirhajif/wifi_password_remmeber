import subprocess
wifiList=subprocess.getoutput("netsh wlan show profiles").replace("All User Profile","").replace(":","").replace("-","").replace("User profiles","").replace("Group policy profiles (read only)","").replace("Profiles on interface WiFi","").replace("<None>","").replace("\n","")
List=wifiList.split()
for i in range(len(List)-2):
    password=subprocess.getoutput("WifiPassword "+List[i])
    print(password)