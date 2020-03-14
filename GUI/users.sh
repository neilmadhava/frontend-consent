#!/bin/bash

token="$1"
command="$2"
arg1="$3"
arg2="$4"
arg3="$5"

chaincodeName="newv3"

if [ $command = "revokeconsent" ]
then
	VALUES=$(curl -s -X POST \
	  http://localhost:4000/channels/mychannel/chaincodes/$chaincodeName \
	  -H "authorization: Bearer $token" \
	  -H "content-type: application/json" \
	  -d "{
	  \"peers\": [\"peer0.airport.example.com\"],
	  \"fcn\":\"revokeConsent\",
	  \"args\":[\"$arg1\", \"$arg2\"]
	}")
	echo $VALUES
fi

if [ $command = "delete" ]
then
	VALUES=$(curl -s -X POST \
	  http://localhost:4000/channels/mychannel/chaincodes/$chaincodeName \
	  -H "authorization: Bearer $token" \
	  -H "content-type: application/json" \
	  -d "{
	  \"peers\": [\"peer0.airport.example.com\"],
	  \"fcn\":\"deletePerson\",
	  \"args\":[\"$arg1\"]
	}")
	echo $VALUES
fi

consent="$(echo $arg2 | awk '{print tolower($0)}')";
if [ $command = "update" ]
then
	VALUES=$(curl -s -X POST \
	  http://localhost:4000/channels/mychannel/chaincodes/$chaincodeName \
	  -H "authorization: Bearer $token" \
	  -H "content-type: application/json" \
	  -d "{
	  \"peers\": [\"peer0.airport.example.com\"],
	  \"fcn\":\"giveConsent\",
	  \"args\":[\"$arg1\", \"$consent\", \"$arg3\"]
	}")
	echo $VALUES
fi

if [ $command = "gethistory" ]
then
	curl -s -X GET \
	  "http://localhost:4000/channels/mychannel/chaincodes/$chaincodeName?peer=peer0.airport.example.com&fcn=getHistoryForPerson&args=%5B%22$arg1%22%5D" \
	  -H "authorization: Bearer $token" \
	  -H "content-type: application/json"
fi
