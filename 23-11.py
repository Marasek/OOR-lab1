# -*- coding: utf-8 -*-
import sys
import threading
import time

class Server(threading.Thread):
    def __init__(self,lock):
        threading.Thread.__init__(self)
        self.lock = lock


    def run(self):#Metoda run jest najwa¿niejsz¹ metod¹ ka¿dego w¹tku,
                  #w której zdefiniowane s¹ wszystkie dzia³ania wykonywane przez w¹tek.
        i = 5

        while i > 0:
            print("Runda", i)
            time.sleep(3)
            i = i - 1

if __name__ == "__main__":

    lock = threading.Lock()#nowa blokada jest tworzona przez wywo³anie funkcji lock() która zwraca nowy obiekt blokadê.
    server = Server(lock)
    server.start() #start() tworzy nowy w¹tek i wywo³uje run()
    running = 1

    while running:
        text = sys.stdin.readline()#strumieñ wejœcia i komunikacji z proesorem
        text = text.strip('\n')#strip pobiera opcjonalny argument okreœlaj¹cy, jakie znaki powinny zostaæ usuniête.

        if text == "koniec":
            running = 0
        else:
            print(text, " *")
    server.join()#metoda join ³¹czy elementy listy w jeden ³añcuch znaków
