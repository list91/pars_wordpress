from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
def create_tabl(ind, r_name,strok,stolb,stolb_index_ABCD):
	driver = webdriver.Chrome()
	l="https://www.rti-prom.ru/wp-admin/admin.php?page=tablepress_add"
	driver.get(l)

	index=ind#номер таблицы
	r_name=r_name#"at-5"
	strok=strok
	stolb=stolb

	'''полное имя таблицы'''
	name=str(index)+"-zubchatye-remni-"+r_name+"-2022-10-07.csv"

	''' авторизация '''
	action = ActionChains(driver)
	login = driver.find_element(By.XPATH,"//*[@id='user_login']")
	password = driver.find_element(By.XPATH,"//*[@id='user_pass']")
	login.send_keys("...")#ввели логин
	password.send_keys("...")#ввели пароль
	#нашли и нажали на кнопку входа
	vhod_btn = driver.find_element(By.XPATH,"//*[@id='wp-submit']")
	action.click(vhod_btn)
	action.perform()

	#short=driver.find_element(By.ID,"table-information-shortcode").get_attribute("value")#шорткод таблицы
	time.sleep(5)
#################################################
	''' задаем параметры таблицы '''
	tabl_name=driver.find_element(By.XPATH,"//*[@id='table-name']")
	inp_strok=driver.find_element(By.XPATH,"//*[@id='table-rows']")
	inp_strolb=driver.find_element(By.XPATH,"//*[@id='table-columns']")

	'''написать название таблицы'''
	tabl_name.send_keys(name)

	'''строки'''
	action.click(inp_strok)
	action.perform()
	inp_strok.send_keys(Keys.BACK_SPACE)
	inp_strok.send_keys(str(strok+1))

	'''столбы'''
	action.click(inp_strolb)
	action.perform()
	inp_strolb.send_keys(Keys.BACK_SPACE)
	inp_strolb.send_keys(str(stolb))

##
	vhod_btn = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[1]/div[3]/form/div/div/div[1]/p[3]/input")
	action.click(vhod_btn)
	action.perform()
	time.sleep(5)
	'''открываем обработанную таблицу в виде файлов "столбцов" '''
	files_finish=[]
	for i in range(1,stolb+1):
		files_read=open('colonka_'+str(i)+'.txt', 'r')
		files_finish.append(files_read)

	for fil, stolbec in zip(files_finish, stolb_index_ABCD):
		for stroka, line_file in zip(range(1,strok+1), fil.readlines()):
			stroka+=1#таблица начинает нумерацию  с 2
			kolonna=stolbec+str(stroka)
			coll = driver.find_element(By.XPATH,"//*[@id='cell-"+kolonna+"']")
			coll.send_keys(line_file)#записать в нее
		fil.close()
