# pip install speedtest-cli
# Measures in bits per second
try:
    import os
    import time
    import platform
    from tqdm import tqdm
    import speedtest as st
    from typing import Union
    from colorama import Fore, init
except ImportError as e_imp:
    print(f"The following import error ocurred: {e_imp}")

init(autoreset=True)

def clear_screen() -> None:
    actual_system = platform.system()

    if actual_system == "Windows":
        os.system("cls")
    elif actual_system == "Linux":
        os.system("clear")
    else:
        print("The script only runs in linux and windows os systems")
        exit()

def print_results(data: dict[str, Union[str, int, float]]) -> None:
    print("\n\n")
    print(Fore.MAGENTA + "="*80)
    print(Fore.GREEN + "INTERNET SPEED TEST RESULTS:".center(80))
    print(Fore.MAGENTA + "="*80)
    print(Fore.CYAN +
        f"Download: {data['download']} | Upload:{data['upload']} | Ping: {data['ping']}".center(80))
    print(Fore.MAGENTA + "-"*80)
    print(Fore.CYAN +
        f"HOST:{data['host']} | ISP:{data['isp']} | LATENCY: {data['latency']}".center(80))
    print(Fore.MAGENTA + "-"*80)

def main_met() -> None:
    data= {}

    print(Fore.GREEN + "GETTING BEST AVAILABLE SERVERS, UPLOADING & DOWNLOADING SPEED.....")
    speed= st.Speedtest()
    speed.get_best_server()
    for i in tqdm(range(100), colour="green", desc="Finding Optimal Server"):
        time.sleep(0.005)
    print("Processing data\n")

    data["ping"] = speed.results.ping
    downReal= speed.download(threads=None)
    for _ in tqdm(range(100), colour="cyan", desc="Getting Download Speed"):
        time.sleep(0.005)
    print("Processing data\n")

    upReal= speed.upload(threads=None, pre_allocate= False)
    for i in tqdm(range(100), colour="red", desc="Getting Upload Speed"):
        time.sleep(0.005)

    # Conversion to real speed contracted
    data["download"] = round(downReal / (10**6), 2)
    data["upload"] = round(upReal / (10**6), 2)
    # print(speed.results)
    data["host"] = speed.results.server["host"]
    data["isp"] = speed.results.client["isp"]
    data["latency"] = speed.results.server["latency"]

    del downReal, upReal

    print_results(data)
    
if __name__== "__main__":
    clear_screen()
    main_met()