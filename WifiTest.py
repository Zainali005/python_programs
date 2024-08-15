import speedtest as st
def speed_test():
    test = st.Speedtest()

    download_speed = test.download();
    download_speed = round(download_speed/10**6,2)
    print("Download speed in Mbps :",download_speed)
    up_speed = test.upload();
    download_speed = round(up_speed/10**6,2)
    print("Upload speed in Mbps :",download_speed)
    
    ping = test.results.ping
    print("Ping :",ping, "ms")

speed_test()