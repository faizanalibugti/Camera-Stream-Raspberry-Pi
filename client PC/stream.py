import cv2
import numpy as np
import requests
import time

while True:
    last_time = time.time()
    url = "http://192.168.1.100:8000/frame.npy"
    r = requests.get(url, allow_redirects=True)

    with open("frame.npy","wb") as npy: 
        for chunk in r.iter_content(chunk_size=1024): 
            # writing one chunk at a time to pdf file 
            if chunk: 
                npy.write(chunk) 
    
    try:
        frame = np.load('./frame.npy', allow_pickle=True)
        cv2.imshow("Stream", frame)
    except:
        #frame = np.load('./frame.npy', allow_pickle=True)
        cv2.imshow("Stream", frame)

    
    print("Delay: {}".format((time.time() - last_time)))
            
    # Press "q" to quit
    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break