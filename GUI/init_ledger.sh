#!/bin/bash
token="$1"

filename="result.txt"
i=0

while read line
do 
    if [ $i == 0 ]
    then 
        userID="\"$line\""
    elif [ $i == 1 ]
    then
        src="\"$line\""
    elif [ $i = 2 ]
    then
        name="\"$line\""
    elif [ $i = 3 ]
    then
        departDate="\"$line\""
    elif [ $i = 4 ]
    then
        phone="\"$line\""
    elif [ $i = 5 ]
    then
        creditCard="\"$line\""
    elif [ $i = 6 ]
    then
        aadhar_id="\"$line\""
    elif [ $i = 7 ]
    then
        email="\"$line\""
    elif [ $i = 8 ]
    then
        consent_type="\"$line\""
    fi

    let "i = $i + 1";
done < $filename

consent="$(echo $consent_type | awk '{print tolower($0)}')";
args="$(echo "$(echo $userID)", "$(echo $src)", "$(echo $name)", "$(echo $departDate)", "$(echo $phone)", "$(echo $creditCard)", "$(echo $aadhar_id)", "$(echo $email)", "$(echo $consent)")"

VALUES=$(curl -s -X POST \
  http://localhost:4000/channels/mychannel/chaincodes/chainv1_3 \
  -H "authorization: Bearer $token" \
  -H "content-type: application/json" \
  -d "{
  \"peers\": [\"peer0.airport.example.com\",\"peer0.ccd.example.com\",\"peer0.users.example.com\"],
  \"fcn\":\"initPerson\",
  \"args\":[$args]
}")
echo $VALUES