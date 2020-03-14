token="$1"
org="$2"
arg="$3"
chaincodeName="newv3"
command="$4"

if [ \( "$org" = "airport" \) -o \( "$org" = "users" \) ]
then
	if [ "$command" = "queryprivate" ]
	then
		curl -s -X GET \
		  "http://localhost:4000/channels/mychannel/chaincodes/$chaincodeName?peer=peer0.airport.example.com&fcn=readPrivatePerson&args=%5B%22$arg%22%5D" \
		  -H "authorization: Bearer $token" \
		  -H "content-type: application/json"
	fi
	if [ "$command" = "querypublic" ]
	then
		curl -s -X GET \
		  "http://localhost:4000/channels/mychannel/chaincodes/$chaincodeName?peer=peer0.airport.example.com&fcn=readPersonPublic&args=%5B%22$arg%22%5D" \
		  -H "authorization: Bearer $token" \
		  -H "content-type: application/json"
	fi
	if [ "$command" = "queryall" ]
	then
		curl -s -X GET \
		  "http://localhost:4000/channels/mychannel/chaincodes/$chaincodeName?peer=peer0.airport.example.com&fcn=getPersonsByRange&args=%5B%22%22%2C%20%22%22%5D" \
		  -H "authorization: Bearer $token" \
		  -H "content-type: application/json"
	fi
fi

if [ "$org" = "ccd" ]
then
	curl -s -X GET \
	  "http://localhost:4000/channels/mychannel/chaincodes/$chaincodeName?peer=peer0.airport.example.com&fcn=readPerson&args=%5B%22$arg%22%2C%20%22$org%22%5D" \
	  -H "authorization: Bearer $token" \
	  -H "content-type: application/json"
fi

if [ "$org" = "mcd" ]
then
	curl -s -X GET \
	  "http://localhost:4000/channels/mychannel/chaincodes/$chaincodeName?peer=peer0.airport.example.com&fcn=readPerson&args=%5B%22$arg%22%2C%20%22$org%22%5D" \
	  -H "authorization: Bearer $token" \
	  -H "content-type: application/json"
fi
