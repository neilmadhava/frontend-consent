#!/bin/bash

token="$1"
command="$2"
arg1="$3"
arg2="$4"

chaincodeName="testv5"

if [ $command = "revokeconsent" ]
then
	VALUES=$(curl -s -X POST \
	  http://localhost:4000/channels/mychannel/chaincodes/$chaincodeName \
	  -H "authorization: Bearer $token" \
	  -H "content-type: application/json" \
	  -d "{
	  \"peers\": [\"peer0.airport.example.com\",\"peer0.ccd.example.com\",\"peer0.users.example.com\"],
	  \"fcn\":\"revokeConsent\",
	  \"args\":[\"$arg1\"]
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
	  \"peers\": [\"peer0.airport.example.com\",\"peer0.users.example.com\"],
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
	  \"peers\": [\"peer0.airport.example.com\",\"peer0.users.example.com\"],
	  \"fcn\":\"giveConsent\",
	  \"args\":[\"$arg1\", \"$consent\"]
	}")
	echo $VALUES
fi