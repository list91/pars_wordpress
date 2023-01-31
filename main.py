import os
import mod

'''функция чтобы создать каталог для хранения колонок(пофиксить)'''
def create_work_catalog(stolbs, txt_name_list):
	os.mkdir("TABL_result")
	for name in txt_name_list:
		os.mkdir("TABL_result/"+name)
		for stolb in range(1,stolbs+1):
			f=open("TABL_result/"+name+"/"+str(stolb)+"-coll_"+name+".txt","w")

"""столбы надо определать автоматически
подготавливаем ориентиры для перемещения по каталогам
для этого извлекаем имена файлов"""
stolbs=3
directory = 'megalinear/'
files = os.listdir(directory)
images = filter(lambda x: x.endswith('.txt'), files)
txt_list=[]
txt_name_list=[]
for i in images:
	txt_list.append(i)
for i in txt_list:
	q=i.replace('.txt','')
	txt_name_list.append(q)
st=1

"""цикл перебора созданных заранее директорий функцией,
 и создание колонок как отдельных файлов(пофиксить все что связанно с колонками)"""
for i in txt_name_list:
###################################################
	r=open("megalinear/"+i+".txt","r", encoding='utf-8')
	collons=[]
	for k in range(1,stolbs+1):
		txt_w=open("TABL_result/"+i+"/"+str(k)+"-coll_"+i+".txt","w", encoding='utf-8')
		collons.append(txt_w)
	w=open("TABL_result/"+i+"/"+str(st)+"-coll_"+i+".txt","w", encoding='utf-8')
	st=1
	for rl in r.readlines():
		for s in rl.split(' 	'):
			
			q=s.replace('\n','')
			qq=q.replace('\t','')
			collons[st-1].write(qq+"\n")
			st+=1
			if st==4:
				st=1
	for v in collons:
		v.close()
	r.close()
###################################################

	"""форматирование строк(пофиксить, избавиться от вспомогательного файла)"""
	fn=open('null.txt').readlines()#null строка
	fn2=open('2-coll_H_WIDE.txt').readlines()
	for j in range(1,stolbs+1):
		files_rea=open("TABL_result/"+i+"/"+str(st)+"-coll_"+i+".txt","r", encoding='utf-8')#открываем в режиме чтения
		files_read_mod=files_rea.readlines()
		for u in files_read_mod:
			if u=='\n':
				files_read_mod.remove(u)
		files_write_mode=open("TABL_result/"+i+"/"+str(st)+"-coll_"+i+".txt","w", encoding='utf-8')#открываем в режиме записи
		files_write_mode.writelines(files_read_mod)
		files_rea.close()
		files_write_mode.close()

#индекс имена столбы 
'''создаем словарь данных наших тхт файлов'''
data={}
for i, j in zip(range(1,len(txt_name_list)+1), txt_name_list):
	r=open("megalinear/"+j+".txt","r", encoding='utf-8')
	data[j]=[len(r.readlines()), stolbs]
	r.close()
print(data)
stolb_index_ABCD=["A","B","C"]
#индекс, имя таблицы, строк, столбов, ABCD
#for i in 
#	mod.create_tabl(ind, r_name,strok,stolb,stolb_index_ABCD)


#for i in data:
#	print(data[i][0])