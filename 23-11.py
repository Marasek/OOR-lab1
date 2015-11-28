# -*- coding: utf-8 -*-
import sys
import threading
import time

class Server(threading.Thread):
    def __init__(self,lock):
        threading.Thread.__init__(self)
        self.lock = lock


    def run(self):#Metoda run jest najwa�niejsz� metod� ka�dego w�tku,
                  #w kt�rej zdefiniowane s� wszystkie dzia�ania wykonywane przez w�tek.
        i = 5

        while i > 0:
            print("Runda", i)
            time.sleep(3)
            i = i - 1

if __name__ == "__main__":

    lock = threading.Lock()#nowa blokada jest tworzona przez wywo�anie funkcji lock() kt�ra zwraca nowy obiekt blokad�.
    server = Server(lock)
    server.start() #start() tworzy nowy w�tek i wywo�uje run()
    running = 1

    while running:
        text = sys.stdin.readline()#strumie� wej�cia i komunikacji z proesorem
        text = text.strip('\n')#strip pobiera opcjonalny argument okre�laj�cy, jakie znaki powinny zosta� usuni�te.

        if text == "koniec":
            running = 0
        else:
            print(text, " *")
    server.join()#metoda join ��czy elementy listy w jeden �a�cuch znak�w
