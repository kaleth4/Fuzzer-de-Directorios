import argparse
import requests
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

# Configuración de nivel profesional
def fuzzer(url_base, word, progress_bar, timeout=5):
    # Asegurar que la URL termine en / y quitar espacios
    url = f"{url_base.rstrip('/')}/{word.strip()}"
    headers = {'User-Agent': 'Pro-Fuzzer-Scanner/1.0'}
    
    try:
        # Usamos stream=True para no descargar el cuerpo, solo ver la cabecera (más rápido)
        response = requests.get(url, headers=headers, timeout=timeout, allow_redirects=False)
        
        if response.status_code == 200:
            progress_bar.write(f"[+] Encontrado (200): {url}")
        elif response.status_code == 301:
            progress_bar.write(f"[*] Redirección (301): {url}")
            
    except requests.RequestException:
        pass # Ignorar errores de conexión para no frenar el proceso
    finally:
        progress_bar.update(1)

def main():
    parser = argparse.ArgumentParser(description="Multi-threaded Directory Fuzzer Pro")
    parser.add_argument("url", help="URL base (ej: http://objetivo.com)")
    parser.add_argument("dict", help="Ruta al diccionario")
    parser.add_argument("-t", "--threads", type=int, default=20, help="Número de hilos (default: 20)")
    args = parser.parse_args()

    try:
        with open(args.dict, 'r', encoding='utf-8', errors='ignore') as f:
            wordlist = f.read().splitlines()

        print(f"[*] Cargadas {len(wordlist)} palabras. Iniciando con {args.threads} hilos...")

        with tqdm(total=len(wordlist), desc="Escaneando", unit="url") as bar:
            # La magia del nivel pro: ejecución en paralelo
            with ThreadPoolExecutor(max_workers=args.threads) as executor:
                for word in wordlist:
                    executor.submit(fuzzer, args.url, word, bar)

    except FileNotFoundError:
        print("[-] Error: Diccionario no encontrado.")
    except KeyboardInterrupt:
        print("\n[!] Escaneo interrumpido por el usuario.")

if __name__ == "__main__":
    main()
