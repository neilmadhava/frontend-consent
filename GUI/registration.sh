username="$1"
org="$2"

ORG_TOKEN=$(curl -s -X POST \
  http://localhost:4000/users \
  -H "content-type: application/x-www-form-urlencoded" \
  -d 'username='$username'&orgName='$org)

ORG_TOKEN=$(echo $ORG_TOKEN | jq ".token" | sed "s/\"//g")
echo $ORG_TOKEN
