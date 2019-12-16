#!/usr/bin/python3
# coding=utf-8
# author=Gepetojj

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("headless")
chrome = webdriver.Chrome(options=options)
fonte = 'https://www.google.com.br/'


def main():
    while True:
        ask = input("\nDigite o tema da pesquisa: ")
        pesquisar(ask)

def pesquisar(tema):
    if tema is None:
        return print("Digite algo como tema.")

    chrome.get(fonte)
    barra = chrome.find_element_by_xpath("//input[@class='gLFyf gsfi']")
    barra.click()
    barra.send_keys(tema)
    barra.send_keys(u'\ue007')
    pegar_textos(tema)

def remover_caracteres(string, to_remove):
    new_string = string
    for x in to_remove:
        new_string = new_string.replace(x, '')
    return new_string

def adicionar_quebra(string):
    new_string = string
    for x in ".":
        new_string = new_string.replace(x, '.\n')
    return new_string

def pegar_textos(tema):
    try:
        link = chrome.find_element_by_partial_link_text("Wikipédia")

    except:
        return print("Não encontrei nada sobre esse tema.")

    else:
        link.click()
        link_atual = chrome.current_url
        print(f"Estou pesquisando no link: {link_atual}\nProcessando resultados...")
        time.sleep(5)

        texto = chrome.find_element_by_tag_name("p").text
        texto_formatado = remover_caracteres(texto, "[]")
        txt_formatado_quebrado = adicionar_quebra(texto_formatado)
        arquivo = open(f"resultados/{tema}.txt", "a")

        with arquivo as arch:
            arch.writelines("Gerado por Pesquisador de Gepetojj\n\n")
            arch.writelines(txt_formatado_quebrado)
            arch.writelines(f"\n\nFonte: {link_atual}")
            arch.writelines("\nCriador: https://github.com/gepetojj")
            print("Arquivo pronto.")


if __name__ == "__main__":
    main()
