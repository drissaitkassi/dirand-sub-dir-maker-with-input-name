import os

video_name=input('MINOUSAAAA PLEASE ENTELL NAME :')

maindir=(r'C:\Users\minousat\Desktop\Hial Wa Tabkh\\')

os.chdir(maindir)

os.mkdir(video_name)

os.chdir(video_name)

os.mkdir(video_name + ' ' + 'audio')

os.mkdir(video_name + ' ' + 'video')

os.mkdir(video_name + ' ' + 'original footage')