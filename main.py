from playwright.sync_api import sync_playwright
import time

with sync_playwright()  as p:
    navegador = p.chromium.launch(headless=False) # headless
    pagina = navegador.new_page()
    pagina.goto("https://www.amazon.com.br/ref=nav_logo") # acessa o site 
    pagina.screenshot(path="screenshot1.png", full_page=True)
    # pagina.locator('xpath=//*[@id="twotabsearchtextbox"]').click() # clica em um elemento especifico do site nesse casso a barra de pesquisa
    pagina.fill('xpath=//*[@id="twotabsearchtextbox"]', "iphone 14") # com o .fill consigo preencher um campo que foi selecionado anteriormente
    pagina.screenshot(path="screenshot2.png", full_page=True)
    pagina.locator('//*[@id="nav-search-submit-button"]').click() # clicar no botão de pesquisar 
    pagina.screenshot(path="screenshot3.png", full_page=True)
    pagina.locator('//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/div/div/div[2]/span/a/div/img').click() # clicar na imagem do primeiro iphone que a parece no resultado da pesquisa
    pagina.screenshot(path="screenshot4.png", full_page=True)
   # pagina.locator('//*[@id="a-autoid-14-announce"]/div/div[1]/img').click() # para trocar a cor do iphone
    pagina.locator('//*[@id="add-to-cart-button"]').click() #clicar no botão de adicinoar ao carrinho 
    pagina.screenshot(path="screenshot5.png", full_page=True)
   # pagina.locator('//*[@id="attachSiNoCoverage"]/span/input').click() # não aceitar o seguro 
    pagina.locator('//*[@id="sc-buy-box-ptc-button"]/span/input').click() #clicar no botão de fechar peidido
    pagina.screenshot(path="screenshot6.png", full_page=True)

    time.sleep(5)
