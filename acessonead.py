from selenium import webdriver

## GET user, senha
usr = input("Insira seu número de matrícula:")
pssd = usr

## abrir site NEAD  
driver = webdriver.Chrome()
driver.get('http://diocesano.nead.marista.edu.br/')

## acessar meu perfil
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

id = driver.find_element_by_xpath('//*[@id="login_username"]')
id.send_keys(usr)

password = driver.find_element_by_xpath('//*[@id="login_password"]')
password.send_keys(pssd)

access = driver.find_element_by_xpath('//*[@id="login"]/div[4]/input')
access.click()
