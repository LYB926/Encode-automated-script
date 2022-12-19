rawPath = "/data/WispChan/youtube_ori/source"
outPath = "/data/WispChan/youtube_ori/output"


for rawVid in ${rawPath}/*
do
    rawName = `basename $rawVid`
    ./x264-r3102-416e3eb --preset slow --subme 9 --bframes 8 --me umh --keyint infinite --tune ssim --qp 32 $rawName -o ${outPath}/${rawName}_32 &&
    ./x264-r3102-416e3eb --preset slow --subme 9 --bframes 8 --me umh --keyint infinite --tune ssim --qp 35 $rawName -o ${outPath}/${rawName}_35 &&
    ./x264-r3102-416e3eb --preset slow --subme 9 --bframes 8 --me umh --keyint infinite --tune ssim --qp 38 $rawName -o ${outPath}/${rawName}_38 &&
    ./x264-r3102-416e3eb --preset slow --subme 9 --bframes 8 --me umh --keyint infinite --tune ssim --qp 41 $rawName -o ${outPath}/${rawName}_41
done
