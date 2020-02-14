token="$1"
org="$2"
arg="$3"

if [ \( "$org" = "airport" \) -o \( "$org" = "users" \) ]
then
	curl -s -X GET \
	  "http://localhost:4000/channels/mychannel/chaincodes/chainv1_3?peer=peer0.$org.example.com&fcn=readPrivatePerson&args=%5B%22$arg%22%5D" \
	  -H "authorization: Bearer $token" \
	  -H "content-type: application/json"
fi

if [ "$org" = "ccd" ]
then
	curl -s -X GET \
	  "http://localhost:4000/channels/mychannel/chaincodes/chainv1_3?peer=peer0.$org.example.com&fcn=readPerson&args=%5B%22$arg%22%5D" \
	  -H "authorization: Bearer $token" \
	  -H "content-type: application/json"
fi
