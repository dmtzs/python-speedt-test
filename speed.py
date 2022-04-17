# pip install speedtest-cli
# Measures in bits per second

import speedtest as st

def mainMet():
    data= {}

    speed= st.Speedtest()
    speed.get_best_server()

    data["ping"]= speed.results.ping
    downReal= speed.download(threads=None)
    upReal= speed.upload(threads=None, pre_allocate= False)

    # Conversion to real speed contracted
    data["download"]= round(downReal / (10**6), 2)
    data["upload"]= round(upReal / (10**6), 2)

    del downReal, upReal

    print(data)
    
if __name__== "__main__":
    mainMet()