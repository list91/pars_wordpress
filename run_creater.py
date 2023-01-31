import os
def create_work_catalog(stolbs, txt_name_list):
	os.mkdir("TABL_result2")
	m="TABL_result2/SHKIF"
	os.mkdir(m)
	for name in txt_name_list:
		os.mkdir("TABL_result/"+name)
		
		for stolb in range(1,stolbs+1):
			f=open(m+name+"/"+str(stolb)+"-coll_"+name+".txt","w")
			

stolbs=3
directory = 'megalinear2/'
files = os.listdir(directory)
images = filter(lambda x: x.endswith('.txt'), files)
txt_list=[]
txt_name_list=[]
for i in images:
	txt_list.append(i)
for i in txt_list:
	q=i.replace('.txt','')
	txt_name_list.append(q)
print(txt_name_list)

create_work_catalog(stolbs, txt_name_list)
