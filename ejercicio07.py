import time
import random
import threading
import asyncio
import multiprocessing

def consulta_bd(id):
    tiempo = random.randint(1, 5)
    print(f"Consulta {id} iniciada ({tiempo}s)")
    time.sleep(tiempo)
    print(f"Consulta {id} finalizada")


def secuencial():
    inicio = time.time()
    for i in range(1, 4):
        consulta_bd(i)
    print("Tiempo total (secuencial):", round(time.time() - inicio, 2), "s\n")

def hilos():
    inicio = time.time()
    threads = []

    for i in range(1, 4):
        t = threading.Thread(target=consulta_bd, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Tiempo total (hilos):", round(time.time() - inicio, 2), "s\n")

async def consulta_bd_async(id):
    tiempo = random.randint(1, 5)
    print(f"Consulta {id} iniciada ({tiempo}s)")
    await asyncio.sleep(tiempo)
    print(f"Consulta {id} finalizada")


async def asincrono():
    inicio = time.time()
    tareas = [consulta_bd_async(i) for i in range(1, 4)]
    await asyncio.gather(*tareas)
    print("Tiempo total (async):", round(time.time() - inicio, 2), "s\n")

def procesos():
    inicio = time.time()
    procesos = []

    for i in range(1, 4):
        p = multiprocessing.Process(target=consulta_bd, args=(i,))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()

    print("Tiempo total (procesos):", round(time.time() - inicio, 2), "s\n")

if __name__ == "__main__":
    print("=== SECUENCIAL ===")
    secuencial()

    print("=== HILOS ===")
    hilos()

    print("=== ASINCRONO ===")
    asyncio.run(asincrono())

    print("=== PROCESOS ===")
    procesos()
