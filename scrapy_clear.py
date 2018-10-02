from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from envi import config

driver = webdriver.Chrome()
driver.get(config["URL_BROKER"])

# LOGIN
fieldCpf = driver.find_element_by_id("identificationNumber")
fieldCpf.clear()
fieldCpf.send_keys(config["BROKER_CPF_CNPJ"])

fieldPassword = driver.find_element_by_id("password")
fieldPassword.clear()
fieldPassword.send_keys(config["BROKER_PASSWORD"])

fieldDataNascimento = driver.find_element_by_class_name("input_date")
fieldDataNascimento.clear()
fieldDataNascimento.send_keys(config["BROKER_DT_NASC"])

bttSignin = driver.find_element_by_class_name("bt_signin")
bttSignin.click()

bttOpen = driver.find_element_by_class_name("left")
bttOpen.click()

# TROCAR SENHA
bttOpenClientMenu = driver.find_element_by_class_name("container_client")
bttOpenClientMenu.click()

linkMeusDados = driver.find_element_by_link_text("Meus Dados")
linkMeusDados.click()

aTagsInLi = driver.find_elements_by_css_selector('li a')
for a in aTagsInLi:
    if not a.is_displayed():
        if "#" in a.get_attribute('href'):
            a.send_keys(Keys.TAB)
            a.click()

# linkSenhas = driver.find_element_by_link_text("Senhas")
# linkSenhas.click()

# fieldOldPassword = driver.find_element_by_class_name("old_password")
# fieldPassword.clear()
# fieldPassword.send_keys(config["BROKER_PASSWORD"])
#
# fieldNewPassword = driver.find_element_by_class_name("password")
# fieldNewPassword.clear()
# fieldNewPassword.send_keys("333444")
#
# fieldConfirmNewPass = driver.find_element_by_class_name("conf_password")
# fieldConfirmNewPass.clear()
# fieldConfirmNewPass.send_keys("333444")
#
# bttUpdatePass = driver.find_element_by_class_name("update_password bt_yellow")
# bttUpdatePass.click()
#
# # DESLOGAR
# bttOpenClientMenu.click()
#
# bttLogout = driver.find_element_by_class_name("bt_logoff")
# bttLogout.click()
