import subprocess
import csv
import pandas
from jedi._compatibility import DummyFile

path1="/Users/pyjain"
path2="/Users/pyjain/Library/Android/sdk/platform-tools"

"To get whole data from a text file and convert it into string"
def find(path):
    with open(path) as myfile:
        data= myfile.read().replace("\n",",")
        return data
        print(data)
 
"To get the selected lines from a text file "
def selected_lines(path,start,end):
    with open(path) as myfile:
        for line in myfile:
            if line.strip() == start:  # Or whatever test is needed
                break    
        l=[]
        for line in myfile:  # This keeps reading the file
            if line.strip() == end:
                break
            l.append(line.replace("\n",","))
        status="".join(l)
        return(status) 
    
"To get some selected lines from a text file"
def find_by_line(path):
    with open(path) as myfile:
        new_list=[]
        for lines in myfile:
            new_list.append(lines)
        length=len(new_list)
        return(new_list[(length-1)])

"To generate a csv file and set column names"   
def add_headers():
    with open("/Users/pyjain/Desktop/android_phone_status.csv",mode= 'w') as csvfile:
        fieldnames = ['Battery Status', "Additional Battery Status",'Wifi Status', 'CPU Status','Memory Status','mSignalStrength']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        return fieldnames
fn=add_headers()

"To feed values in the csv file "
def csv_file(f_n,battery_status,add_battery_sts,wifi_status,cpu_status,mem_status,m_signalstrength):
    with open("/Users/pyjain/Desktop/android_phone_status.csv",mode= 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=f_n)
        writer.writerow({'Battery Status': battery_status,"Additional Battery Status":add_battery_sts, 'Wifi Status': wifi_status, 'CPU Status': cpu_status, 'Memory Status': mem_status,'mSignalStrength':m_signalstrength})

"Generate different text files for different activities and make a csv file using above functions"
while(1):
    subprocess.call(path2+"/adb shell dumpsys battery >" + path1+"/battery.txt",shell=True)
    subprocess.call(path2+"/adb shell dumpsys wifi >" + path1+"/wifi.txt",shell=True)
    subprocess.call(path2+"/adb shell dumpsys cpuinfo >" + path1+"/cpu.txt",shell=True)
    subprocess.call(path2+"/adb shell cat /proc/meminfo >" + path1+"/meminfo.txt",shell=True)
    subprocess.call(path2+"/adb shell dumpsys batterystats >" + path1+"/batterystatus.txt",shell=True)
    subprocess.call(path2+"/adb shell dumpsys telephony.registry | grep -i signalstrength >" + path1+"/msignalstrength.txt",shell=True)
    
    battery_sts=find(path1+"/battery.txt")
    wifi_sts=selected_lines(path1+"/wifi.txt","WifiConfigManager - Configured networks Begin ----" , "WifiConfigManager - Configured networks End ----")
    cpu_sts=find_by_line(path1+"/cpu.txt")
    mem_info=find(path1+"/meminfo.txt")
    addt_battery_sts=selected_lines(path1+"/batterystatus.txt", "CONNECTIVITY POWER SUMMARY START", "CONNECTIVITY POWER SUMMARY END")
    msignalstrength=find(path1+"/msignalstrength.txt")
    csv_file(fn,battery_sts,addt_battery_sts,wifi_sts,cpu_sts,mem_info,msignalstrength)
