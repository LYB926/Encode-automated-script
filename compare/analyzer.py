from file_read_backwards import FileReadBackwards
import matplotlib.pyplot as plt
#rawName = input('Raw video name:   ')
#QPList  = ['22', '24', '26', '28', '32', '35', '38', '41']
rawName  = 'apple_tree_1920x1080_30'
para     = input('Parameter (e.g. EPZS&16x16&SR=24&RF=2): ')
QPList   = ['41', '38', '35', '32', '28', '26']
BRList   = []
PSNRList = []
SSIMList = []
for qp in QPList:
    logName = 'compare/' + rawName + "_" + qp + ".log"
    cnt = 0
    with FileReadBackwards(logName, encoding="utf-8") as BigFile:
    # getting lines by lines starting from the last line up
        for line in BigFile:
            if (cnt==11):
                lineSSIM = line
            if (cnt==14):
                linePSNR = line
            if (cnt==6):
                lineBitrate = line
            cnt = cnt + 1
    BRList.append((float(lineBitrate[37:])) /1000)
    PSNRList.append(float(linePSNR[40:-22]))
    SSIMList.append(float(lineSSIM[37:]))
#print (BRList,SSIMList,PSNRList)

x264 = [24.08, 26.72, 30.851629, 32.576346, 33.686060, 35.41703, 36.49]
baseline = [27.00, 28.349293, 32.20 ,33.87, 35.0, 36.67, 37.6]
br264 = [0.7, 1, 2, 3, 4, 6, 8]
jm   = [29.468,31.420,33.309,35.134,37.396,38.408]
brjm= [0.936, 1.281, 1.806,2.679,5.150,7.497]
plt.plot(br264,x264, label='x264', marker='.')
plt.plot(br264,baseline, label='20% better than x264',linestyle='dashed')
plt.plot(brjm,jm, label='JM Encoder (Original)', marker='^')

labelJM = 'JM Encoder (' + para + ')'
plt.plot(BRList, PSNRList, label=labelJM, marker='h')
plt.xlabel('Bitrate, Mbps')
plt.ylabel('PSNR(Y), dB') 
plt.title('Bitrate/quality, PSNR metric')  
plt.legend()
plt.savefig("./" + para + '.png')
plt.show()