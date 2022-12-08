import os

def generate(rawName):
    # Automated generating Linux bash script for x264 encoding
    # init
    encoderName = 'x264-r3102-416e3eb'
    rawPath = '/data/CAOYUE/MSU2021/'
    # rawName = input('Raw video name:  ')  #Assume name is 'apple_tree_1920x1080_30.yuv'
    rawNameSplit = rawName.split('.')       #Result: ['apple_tree_1920x1080_30', 'yuv']
    tempSplit = rawNameSplit[0].split('_')  #Result: ['apple', 'tree', '1920x1080', '30']
    for w in tempSplit:
        if w == '1920x1080':
            rawResolution = w
        elif w == '1440x1080':
            rawResolution = w
    
    for w in tempSplit:
        if w == '30':
            rawFrameRate = w
        elif w == '52':
            rawFrameRate = w
        elif w == '25':
            rawFrameRate = w
        elif w == '24':
            rawFrameRate = w
        elif w == '60':
            rawFrameRate = w
        elif w == '39':
            rawFrameRate = w
        elif w == '50':
            rawFrameRate = w

    outputPath = '/data/WispChan/x264_benchmark_output/'+rawNameSplit[0]+'/'
    bitrateList = ['700', '1000', '2000', '3000', '4000', '6000',
                   '8000', '10000']  # --bitrate <integer>     Set bitrate (kbit/s)

    # Creat file
    fileName = rawNameSplit[0] + '_' + 'x264.sh'
    file = open(fileName, mode='w', encoding='utf-8')
    file.write('mkdir /data/WispChan/x264_benchmark_output/' +
               rawNameSplit[0] + '\n')

    # Write to file
    for bitrate in bitrateList:
        cmd = './' + encoderName + ' --preset slow --subme 9 --bframes 8 --me umh --keyint infinite --tune ssim --bitrate '\
            + bitrate + ' ' + rawPath + rawName + ' --input-res ' + rawResolution + ' --fps ' \
            + rawFrameRate + ' -o ' + outputPath + \
            rawNameSplit[0] + '_' + bitrate + '.264\n'
        file.write(cmd)

    file.close()

    os.system('chmod 777 ' + fileName)


fileNameAll = 'encode_x264_all.sh'
file = open(fileNameAll, mode='w', encoding='utf-8')
sequences = ['apple_tree_1920x1080_30.yuv', 'asteroid_landing_1920x1080_25.yuv', "baseball_1920x1080_60.yuv", "boat_1920x1080_60.yuv", "boring_concert_1920x1080_30.yuv", "carpets_1920x1080_25.yuv", "cgi_cricket_1920x1080_25.yuv", "chili_pepper_1920x1080_60.yuv", "christmas_cats_1920x1080_25.yuv", "city_1920x1080_25.yuv",
             "crowd_run_1920x1080_50.yuv", "diy_mixer_1920x1080_25.yuv", "epic_clip_1920x1080_24.yuv", "fifa_1920x1080_52.yuv", "fishing_1920x1080_25.yuv", "forest_eye_1920x1080_25.yuv", "graycolor_concert_1920x1080_24.yuv", "green_grass_1920x1080_30.yuv", "hard_rock_1920x1080_25.yuv", "keeping_warm_1920x1080_30.yuv", "kids_1920x1080_30.yuv", "lecture_1440x1080_25.yuv", "lemonade_ads_1920x1080_25.yuv", "mobile_1920x1080_24.yuv", "mordor_gameplay_1920x1080_39.yuv", "mosquito_1920x1080_30.yuv", "mosquito_movie_1920x1080_24.yuv", "motobike_1920x1080_24.yuv", "motofootball_1920x1080_50.yuv", "mountains_1920x1080_30.yuv", "new_york_1920x1080_24.yuv", "nfl_1920x1080_30.yuv", "night_concert_1440x1080_30.yuv", "night_sky_1920x1080_24.yuv", "night_walk_1920x1080_24.yuv", "old_ship_1920x1080_60.yuv", "orchestra_1920x1080_25.yuv", "painting_slideshow_1920x1080_30.yuv", "photo_art_1920x1080_24.yuv", "road_timelapse_1920x1080_30.yuv", "roller_girl_1920x1080_24.yuv", "seawave_1920x1080_24.yuv", "shakerwalk_1920x1080_25.yuv", "sheriff_1920x1080_30.yuv", "skiing_1920x1080_25.yuv", "strange_clip_1920x1080_25.yuv", "street_report_1920x1080_60.yuv", "street_views_1920x1080_25.yuv", "townday_1920x1080_30.yuv", "tractor_1920x1080_25.yuv", "water_flow_1920x1080_24.yuv"]
for raw in sequences:
    generate(raw)
    rawSplit = raw.split('.')       #Result: ['apple_tree_1920x1080_30', 'yuv']
    file.write('./' + rawSplit[0] + '_' + 'x264.sh')
    if raw != sequences[50]:
        file.write(' && ')

os.system('chmod 777 ' + fileNameAll)