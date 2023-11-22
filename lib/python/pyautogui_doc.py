"""Funções com pyautogui"""
# import time
import pyautogui
import pyperclip


# função para procurar e ativar a janela
def returntowindow(pjanela):
    """Iniciar janela"""
    # Obter uma lista de janelas com o título "Minha Janela"
    janelas = pyautogui.getWindowsWithTitle(pjanela)

    # Selecionar a primeira janela na lista (se houver)
    if janelas:
        minha_janela = janelas[0]
        # Ativar a janela
        minha_janela.activate()
        # pyautogui.click()


# função para encontrar coordenada
# def get_coordinates():
#     "Pegar coordenadas"
#     print("Mova o cursor para a posição desejada...")
#     time.sleep(5)  # Aguarde alguns segundos para mover o cursor

#     x, y = pyautogui.position()
#     return x, y


# Chame a função para obter as coordenadas
# coord_x, coord_y = get_coordinates()

# print(f"Coordenadas encontradas: x = {coord_x}, y = {coord_y}")


def informar_descricao(texto):
    """
    Copia o texto com acento para a área de transferência e, em seguida, cola-o no campo de entrada.
    Certifique-se de ter definido corretamente o layout do teclado para a colagem funcionar.
    """
    pyperclip.copy(texto)  # Copia o texto com acento para a área de transferência
    pyautogui.hotkey("ctrl", "v")  # Cole o texto com acento do clipboard
