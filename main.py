import pymongo

#please enter you mongdb compass srv or local ip location in client client=pymongo.MongoClient()
#example:
#client=pymongo.MongoClient('mongodb+srv://user1:user1@cluster0.cidxf.mongodb.net/test')

client=pymongo.MongoClient('')


db=client["telecom_directory"]
inform=db.T1
record=	{
			"name": "krish",
			"telephone":9345763412,
			"place":"chennai"
		}
doc=[]
doc.append({
			"name": "jane",
			"telephone":9345793416,
			"place":"coimbator"

		})
doc.append({
			"name": "ramesh",
			"telephone":9245363611,
			"place":"mumbai"
		})
doc.append({
			"name": "vinayak",
			"telephone":9125762411,
			"place":"bangalore"
		})
doc.append({
			"name": "john",
			"telephone":9995722412,
			"place":"kolkata"
		})
doc.append({
			"name": "mick",
			"telephone":9889722412,
			"place":"delhi"
		})
doc.append({
			"name": "mick",
			"telephone":896541235,
			"place":"hydrabad"
		})


inform.insert_one(record)


inform.insert_many(doc)

print("\n\n\n\n")
print("++++++++++++ find  one ++++++++++++")
print("\n\n\n\n")

print(inform.find_one({'name':'mick'}),"\n")

print("\n\n\n\n")
print("++++++++++++ find  one after update one ++++++++++++")
print("\n\n\n\n")

print("before:")
print(inform.find_one({'name':'mick'}),"\n")

inform.update_one({'name':'mick'},{"$set":{'place':'chennai'}})

print("after:")
print(inform.find_one({'name':'mick'}),"\n")


print("\n\n\n\n")
print("++++++++++++ delete one ++++++++++++")
print("\n\n\n\n")
print("before:")
print(inform.find_one({'name':'john'}),"\n")

inform.delete_one({'name':'john'})

print("after:")
print(inform.find_one({'name':'john'}),"\n")

print("\n\n\n\n")
print("++++++++++++ find  many ++++++++++++")
print("\n\n\n\n")


findmany=inform.find()
for i in findmany:
	print(i)

inform.delete_many({"name":"mick"})

print("\n\n\n\n")
print("++++++++++++ after delete many ++++++++++++")
print("++++++++++++ deleted mick ++++++++++++")
print("\n\n\n\n")

findmany=inform.find()
for i in findmany:
	print(i)

inform.update_many({'telephone':9345793416},{"$set":{'name':"plip"}})

print("\n\n\n\n")
print("++++++++++++ after update many ++++++++++++")
print("\n\n\n\n")

findmany=inform.find()
for i in findmany:
	print(i)


client.close()