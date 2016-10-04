query="{query}"

name=$(echo $query | awk -F ' ' '{printf("%s", $1)}{for (i = 2 ; i < NF ; i++) printf(" %s", $i)}')

password=$(echo $query | awk -F ' ' '{printf("%s", $NF)}')

networksetup -setairportnetwork en0 "$name" "$password"
