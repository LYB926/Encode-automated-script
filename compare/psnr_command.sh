ffmpeg -s 1920x1080 -r 30 -pix_fmt yuv420p -i /data/CAOYUE/MSU2021/apple_tree_1920x1080_30.yuv -r 30 -i DOOM99.264 -lavfi psnr="psnr.log" -f null -
ffmpeg -s 1920x1080 -r 30 -pix_fmt yuv420p -i /data/CAOYUE/MSU2021/apple_tree_1920x1080_30.yuv -r 30 -i /data/WispChan/x264_benchmark_output/apple_tree_1920x1080_30/apple_tree_1920x1080_30_6000.264 -lavfi psnr="psnr.log" -f null -
