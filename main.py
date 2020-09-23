import libconf

# with open('libformat.cfg') as f:
# 	config = libconf.load(f)


# data = {'BE_HVAC_OID': { "list" : ({"objName" : "abc", "objOid" : "123"}, {"objName" : "abc"} )}}


# dataapp = data['BE_HVAC_OID']['list']+data['BE_HVAC_OID']['list']
# data['BE_HVAC_OID']['list'] = dataapp

# print(data)



# with open('example.cfg', 'w') as f:
#   libconf.dump(data, f) 


import memory_profiler
# import time
# def check_even(numbers):
# 	even = []
# 	for num in numbers:
# 		if num % 2 == 0:
# 			even.append(num*num)
# 	return even

def check_even(numbers):
	for num in numbers:
		if num % 2 == 0:
			yield num * num 

if __name__ == '__main__':
	m1 = memory_profiler.memory_usage()
	# t1 = time.clock()
	cubes = check_even(range(10000))
	# t2 = time.clock()
	m2 = memory_profiler.memory_usage()
	# time_diff = t2 - t1
	mem_diff = m2[0] - m1[0]
	print(cubes)
	print(f"It took  Secs and {mem_diff} Mb to execute this method ")

 
# BE_HVAC_OID =
# {
#     list =
#     (
#         {
#             objName = "indoor_temp";
#             objOid = "1,3,6,1,4,1,45391,62,1,2,47,0";
#         },
#         {
#             objName = "outdoor_temp";
#             objOid = "1,3,6,1,4,1,45391,62,1,2,48,0";
#         }
#     );
# };
# data = {'BE_HVAC_OID':({'list': ({'obj' : 'obj', 'objid' : '1,2,3'},{'obj' : 'obj', 'objid' : '1,3,4,5'})})};


# with open('libformat.cfg') as f:
# 	config = libconf.load(f)

	# libconf.dump(config, fw) 
	# config.dumps(data)
	# print(f)
# print(libconf.dumps(data))
# print(config)




# 	# sxc = AttrDict(x)
# 	data_list = []
# 	# print(x.objname)
# new_list = []
# for x in config.BE_HVAC_OID.list:
# 	print(x)
# 	print(x.objOid)
# 	new_list.append([('objName' , 'nadeem'), ('objOid' , '1')])

	# new_list.append([3, 4])
# 	x.objName = "nadeem"
# 	x.objOid = "nadeem123"
# # 	# print(x.objName)
# # 	data_list.append(x.objName, x.objOid)

# data = {'BE_HVAC_OID':({'list': new_list})}

# data = {'BE_HVAC_OID': { "list" : ({"objName" : "abc", "objOid" : "123"}, {"objName" : "abc"} )}}

# for x in data["BE_HVAC_OID"]['list']:
# 	print(x.update({"objName" : "updated"}))

# dataapp = data['BE_HVAC_OID']['list']+data['BE_HVAC_OID']['list']
# data['BE_HVAC_OID']['list'] = dataapp

# print(data)
# print(data['BE_HVAC_OID']['list']+data['BE_HVAC_OID']['list'])

# add_tuple = data['BE_HVAC_OID']['list']
# # print(data)
# data = deque(data['BE_HVAC_OID']['list']) 
# data.appendleft(add_tuple) 
# # data =  config["BE_HVAC_OID"]['list'].insert(data["BE_HVAC_OID"]['list'])
# print(data)

# data = {'BE_HVAC_OID':
# 	(
# 		{'list':
# 			(
# 				{
# 		            objName = "obj1";
# 		            objid = "1,3,6,1,4,1,45391,62,1,2,47,0";
# 		        },
# 		        {
# 		            objName = "outdoor_temp";
# 		            objOid = "1,3,6,1,4,1,45391,62,1,2,48,0";
# 		        }
# 			)
# 		}
# 	)
# };




# config.BE_HVAC_OID.list[0].objName = "updated"
# print(libconf.dumps(data)) 

# config['RTL_test']['My_model']['ignore'] = 'updated'
# print(config.BE_HVAC_OID.list[0].objName)

# write
# with open('libformat.cfg', 'w') as f:
# 	libconf.dump(data, f) 

# print(config)


# for x in config.BE_HVAC_OID.list:
# 	# isinstance(x, AttrDict)
# 	print(x)

# with io.open('libformat.cfg') as f:
# 	config = libconf.load(f)

# print(config)

# read
# with open('example.cfg') as f:
#   config = libconf.load(f)

# config['RTL_test']['My_model']['ignore'] = 'updated'

# # write
# with open('example.cfg', 'w') as f:
#   libconf.dump(data, f) 


# print(config.BE_HVAC_OID.list)

# data = {
# 	list : 
# 	(
# 		{
# 			objname : "indoor",
# 			objid : "1,2,3.x"
# 		},
# 		{
# 			objname : "indoor",
# 			objid : "1,2,3.x"
# 		}
# 	)
# };




# print(libconf.dumps({'size': [10, 15], 'flag': True}))
# print(libconf.dumps({"BE_HVAC_OID": list["objName": "nadeem" "objOid": "1,2,3" ]}))



# print(libconf.dumps(data))
# print(libconf.dumps({"1","2","3"}))


# print(config)



