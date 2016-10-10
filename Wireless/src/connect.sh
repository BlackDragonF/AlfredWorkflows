query=$1
#Get curent Wi-Fi interface
interface=$(networksetup -listallhardwareports | grep -C 1 Wi-Fi | tail -n 1 | awk -F ':' '{print $NF}')
#Get SSID
name=$(echo $query | awk -F ' ' '{printf("%s", $1)}{for (i = 2 ; i < NF ; i++) printf(" %s", $i)}')
#Get Password
password=$(echo $query | awk -F ' ' '{printf("%s", $NF)}')

#Check Wi-Fi interface
if [$interface = '']
then
    echo "No Wi-Fi interface found"
else
    #Check Wi-Fi power
    power=$(networksetup getairportpower $interface | awk -F ' ' '{print $NF}')
    if [$power = 'Off']
    then
        echo "Current Wi-Fi interface is off"
    else
        networksetup -setairportnetwork $interface "$name" "$password"
    fi
fi
