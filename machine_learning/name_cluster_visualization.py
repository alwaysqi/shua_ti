import sys,os
import Image


def merge(imglist,output):
    picsize=150
    cur_width = 0
    cur_height= 20
    nth=0
   # size=min(len(imglist),100)
    size=min(len(imglist),300)
   # width = 1500
    width = 3000
    nEachRow=width/picsize
   # height = 20+min(picsize+(size-1)/nEachRow*picsize,750)
    height = 20+min(picsize+(size-1)/nEachRow*picsize,2250)
    row_num=(height-20)/picsize
    merge_img = Image.new('RGB', (width,height), 0xffffff)
    step = len(imglist)/300 + 1
    for i in range(0, len(imglist),step):
        img = imglist[i]
        nth += 1
        if not os.path.exists("imgs/"+img):
                os.system("wget http://192.168.3.253:9333/"+img+" -P imgs/ >/dev/null 2>&1")
        fp = open("imgs/"+img,'r')
        img = Image.open(fp)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        merge_img.paste(img.resize((picsize,picsize),Image.BICUBIC), (cur_width, cur_height))
        cur_width += picsize
        if nth%nEachRow==0:
            cur_height+=picsize
            cur_width=0
        if nth==nEachRow*row_num:
            break
    merge_img.save(output,quality=100)

if __name__ == '__main__':
    name, label , labels_align = '', '', ''
    if len(sys.argv) == 4:
        name_labels_file = sys.argv[1]
        labels_align = sys.argv[2]
        name = sys.argv[3]
        label = os.popen("grep " + name + ' ' + name_labels_file).read().strip().split(' ')[1]
    elif len(sys.argv) == 3:
        labels_align = sys.argv[1]
        label = sys.argv[2]
    else:
        print len(sys.argv)
        print 'stdin is wrong'
    lines = os.popen("cat "+labels_align+" | "+"grep "+'"'+label+" "+'"').read().splitlines()
   # print "cat "+labels_align+" | "+"grep "+'"'+label+" "+'"'
     # lines.sort()
    print lines
    res = []
    count = 0
    for i in lines:
        if i.split(' ')[0] == label:
            res.append(i.split(' ')[1])
            count += 1
    #     else:
    #         if mark:
    #             break
    #         else:
    #             continue
    merge(res, label+'-'+str(count)+'.jpg')
