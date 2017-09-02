import datetime
import random
i=0
while i< 100:
    f = open('C:\Python33\helloworld.csv', 'a')
    f.write('\n202284221,4.0.0,SDPICK,REQU_USERCONTEXT,162810,1,')
    f.write('{:%Y%m%d}'.format(datetime.datetime.now())) #20170504
    f.write('{:,%H%M%S}'.format(datetime.datetime.now())) #111657
    f.write(',202284220170504111657,1,,,,,,,,')
    f.write('Sanku Sinha') #Sanku Sinha
    f.write(',,,,,,,,,')
    f.close()
    #print(i)
    i += 1
