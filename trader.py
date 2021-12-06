from tradingview_ta import TA_Handler, Interval, Exchange
import tradingview_ta as trd
import time
import requests


f = open("result.txt", "a+")


listOfAnalysis = ["BINANCE:DOGEBUSD","BINANCE:SHIBBUSD","BINANCE:SANDBUSD","BINANCE:GALABUSD","BINANCE:AVAXUSDT","BINANCE:NUUSDT","BINANCE:TLMBUSD","BINANCE:FUNUSDT","BINANCE:GRTUSDT","BINANCE:SNXBUSD", "BINANCE:LUNABUSD", "BINANCE:ALICEBUSD", "BINANCE:ROSEBUSD", "BINANCE:ENSBUSD", "BINANCE:DARBUSD", "BINANCE:MATICBUSD", "BINANCE:BATBUSD", "BINANCE:LRCBUSD", "BINANCE:CHRBUSD", "BINANCE:FILBUSD"]

keyOfAnalysis = ["DOGE", "SHIB", "SAND", "GALA", "AVAX", "NU", "TLM", "FUN", "GRT", "SNX", "LUNA", "ALICE", "ROSE", "ENS", "DAR", "MATIC", "BAT", "LRC", "CHR", "FIL"]

#this api key will be yours. You can take it from cryptocompare.com
api_key = ""



counter = 0
while(True):
    analysis = trd.get_multiple_analysis(screener="crypto", interval="2h",symbols=listOfAnalysis)
    BUY_THRESHOLD = 10
    
    for i in range(len(listOfAnalysis)):
        buy = str(analysis[listOfAnalysis[i]].summary["BUY"])
        sell = str(analysis[listOfAnalysis[i]].summary["SELL"])
        neutral = str(analysis[listOfAnalysis[i]].summary["NEUTRAL"])
        response = requests.get("https://min-api.cryptocompare.com/data/price?fsym="+ keyOfAnalysis[i] +"&tsyms=USD")
        result  = keyOfAnalysis[i] + "  " + "B:"+buy + "  " + "S:"+sell + "  " + "N:"+neutral + "  " + "P:"+str(response.json()["USD"]) + "\n"
        f.write(result)
    
    f.write('\n')
    f.write('\n')
    f.write('\n')
    counter+=1
    print(counter)
    f.flush()
    time.sleep(7200)


file.close()
