import ctypes
awareness = ctypes.c_int()
ctypes.windll.shcore.SetProcessDpiAwareness(2)
from mss import mss
from PIL import Image 
import win32gui
import time
import keyboard, mouse
import sys, os
import json
import ocr
import ArtsInfo
if len(sys.argv)>1:
    bundle_dir = sys.argv[1]
else:
    bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
#os.path.basename(sys.executable.lower())[:6]!='python' and 
if not is_admin():
    # Re-run the program with admin rights
    # ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv+[bundle_dir]), None, 1)
    input('请在右键菜单选择以管理员模式运行')
    exit(0)

def captureRect(rect):
    with mss() as sct:
        monitor = {"top": rect[0], "left": rect[1], "width": rect[2], "height": rect[3]}
        sct_img = sct.grab(monitor)
        # Convert to PIL/Pillow Image
        return Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')

def captureWindow(hwnd, local_rect=None):
    if local_rect is None:
        local_rect = win32gui.GetClientRect(hwnd)
    else:
        local_rect = tuple([int(round(i)) for i in local_rect])
    screen_rect = [*local_rect]
    screen_rect[:2] = win32gui.ClientToScreen(hwnd, local_rect[:2])
    screen_rect[2:] = win32gui.ClientToScreen(hwnd, local_rect[2:])
    return captureRect([screen_rect[1], screen_rect[0], screen_rect[2]-screen_rect[0], screen_rect[3]-screen_rect[1]])

def waitSwitched(art_center_x, art_center_y, min_wait=0.1, max_wait=3):
    total_wait = 0
    while True:
        pix = captureWindow(hwnd, (art_center_x-art_width/2-art_expand, art_center_y, art_center_x-art_width/2-art_expand+1.5, art_center_y+1.5))
        if sum(pix.getpixel((0,0)))/3>200:
            return True
        else:
            time.sleep(min_wait)
            total_wait += min_wait
        if total_wait>max_wait:
            return False

def decodeValue(v):
    if type(v)!=str:
        return v
    if "%" in v:
        return float(v[:-1])/100
    else:
        return int(v.replace(',', '').replace('+', ''))

def saveArtifact(info):
    global result

    def buildTag(name, value):
        name = ArtsInfo.AttrName2Ids[name]
        value = decodeValue(value)
        if type(value) == float and (name+'_PERCENT') in ArtsInfo.AttrNamesGensinArt:
            name += '_PERCENT'
        return {
            'name': ArtsInfo.AttrNamesGensinArt[name],
            'value': value
        }

    try:
        typeid = ArtsInfo.TypeNames.index(info['type'])
        typename = ArtsInfo.TypeNamesGenshinArt[typeid]
        setid = [i for i,v in enumerate(ArtsInfo.ArtNames) if info['name'] in v][0]
        setname = ArtsInfo.SetNamesGenshinArt[setid]
        detailname = info['name']
        maintag = buildTag(info['main_attr_name'], info['main_attr_value'])
        normaltags = [
            buildTag(*info[tag].split('+'))
            for tag in sorted(info.keys()) if "subattr_" in tag
        ]
        level = decodeValue(info['level'])
        star = info['star']
        result[typename].append(
            {
                "setName": setname,
                "position": typename,
                "detailName": detailname,
                "mainTag": maintag,
                "normalTags": normaltags,
                "omit": False,
                "id":art_id,
                'level': level,
                'star': star
            }
        )
        return True
    except:
        return False



def scanRows(rows):
    global art_id
    global saved
    art_center_x = first_art_x+(art_width+art_gap_x-0.5)*0+art_width/2
    art_center_y = first_art_y +(art_height+art_gap_y-0.5)*rows[0]+art_height/2
    mouse.move(left+art_center_x, top+art_center_y)
    mouse.click()
    for art_row in rows:
        for art_col in range(art_cols):
            if stopped:
                return False
            if waitSwitched(art_center_x, art_center_y, min_wait=0.1, max_wait=3):
                art_img = captureWindow(hwnd, (art_info_left, art_info_top, art_info_left+art_info_width, art_info_top+art_info_height))
                if art_col==art_cols-1:
                    art_row += 1
                    art_col = 0
                else:
                    art_col += 1
                if art_row in rows:
                    art_center_x = first_art_x+(art_width+art_gap_x-0.5)*art_col+art_width/2
                    art_center_y = first_art_y +(art_height+art_gap_y-0.5)*art_row+art_height/2
                    mouse.move(left+art_center_x, top+art_center_y)
                    mouse.click()
                info = ocr_model.detect_info(art_img)
                if saveArtifact(info):
                    saved += 1
                else:
                    art_img.save(f'artifacts/{art_id}.png')
                    json.dump(info, open(f"artifacts/{art_id}.json", "wt"))
                art_id += 1
                print(f"\r已扫描{art_id}个圣遗物，已保存{saved}个", end='')
            else:
                return False
    return True

def alignFirstRow():
    pix = captureWindow(hwnd, (scroll_fin_keypt_x, scroll_fin_keypt_y, scroll_fin_keypt_x+1.5, scroll_fin_keypt_y+1.5))
    if pix.getpixel((0,0))[0]!=233 or pix.getpixel((0,0))[1]!=229 or pix.getpixel((0,0))[2]!=220:
        for _ in range(3):
            mouse.wheel(1)
        time.sleep(0.1)
        scrollToRow(0)
    

def scrollToRow(target_row, max_scrolls=20):
    in_between_row = False
    rows_scrolled = 0
    lines_scrolled = 0
    while True:
        pix = captureWindow(hwnd, (scroll_fin_keypt_x, scroll_fin_keypt_y, scroll_fin_keypt_x+1.5, scroll_fin_keypt_y+1.5))
        if pix.getpixel((0,0))[0]!=233 or pix.getpixel((0,0))[1]!=229 or pix.getpixel((0,0))[2]!=220:
            # if in_between_row==False:
            #     print('到行之间了')
            in_between_row = True
        elif in_between_row:
            in_between_row = False
            rows_scrolled += 1
            lines_scrolled = 0
            # print(f'已翻{rows_scrolled}行')
            if rows_scrolled >= target_row:
                return rows_scrolled
        if lines_scrolled > max_scrolls:
            return rows_scrolled
        for _ in range(6 if lines_scrolled==0 and target_row>0 else 1):
            mouse.wheel(-1)
            lines_scrolled += 1
            # print('翻一下')
        time.sleep(0.05)

window_name_cn = '原神'
window_name_en = 'Genshin Impact'

hwnd = win32gui.FindWindow(None, window_name_cn)
if hwnd is None or hwnd==0:
    hwnd = win32gui.FindWindow(None, window_name_en)
    
if hwnd is None or hwnd==0:
    input('未找到在运行的原神')
    exit()

w,h = win32gui.GetClientRect(hwnd)[2:]

left, top = win32gui.ClientToScreen(hwnd, (0,0))


if w==0 or h==0:
    print("不支持独占全屏模式")
    exit()

if abs(w/h-2560/1440)>0.05:
    print('请将原神设定成16:9分辨率')
    exit()


# initialization
ocr_model = ocr.OCR(scale_ratio=min(w/2560, h/1440), model_path=os.path.join(bundle_dir, 'mn_model.h5'))
art_id = 0
saved = 0
stopped = False
result = {"version":"1", "flower":[], "feather":[], "sand":[], "cup":[], "head":[]}

def to_stop():
    global stopped
    stopped = True
mouse.on_middle_click(to_stop)

# All Parameters
DRY_RUN = False
art_cols = 7
art_rows = 5

first_art_x = 276/2560*w
first_art_y = 161/1440*h
art_width = 165/2560*w
art_height = 203/1440*h
art_expand = 6/2560*w

art_gap_x = 31/2560*w
art_gap_y = 31/1440*h

art_info_top = 160/1440*h
art_info_left = 1723/2560*w
art_info_width = 656/2560*w
art_info_height = 1119/1440*h

scroll_keypt_x = 435/2560*w
scroll_keypt_y = 1270/1440*h

# # star color=255,204,50
# scroll_fin_keypt_x = 358
# scroll_fin_keypt_y = 320

# margin near level number, color=233,229,220
scroll_fin_keypt_x = 285/2560*w
scroll_fin_keypt_y = 335/1440*h

if not DRY_RUN:
    os.makedirs('artifacts', exist_ok=True)


input('请打开圣遗物背包界面，最好翻到圣遗物列表最上面。按回车继续')
input('运行期间请保持原神在前台，请勿遮挡窗口或操作鼠标，按鼠标中键停止。按回车继续')
input('开始后将尝试自动对齐第一行以方便识别，若对齐结果有误，请立刻按中键停止。按回车开始执行')
print('程序将于5秒后自动开始运行，若此条提示显示时未自动切换到原神窗口，请手动点击原神窗口切到前台')

keyboard.press('alt')
win32gui.ShowWindow(hwnd,5)
win32gui.SetForegroundWindow(hwnd)
keyboard.release('alt')

time.sleep(5)

print('正在自动对齐')
mouse.move(left+first_art_x, top+first_art_y)
alignFirstRow()
print('对齐完成，即将开始扫描')
time.sleep(0.5)
start_row = 0
while True:
    if stopped or not scanRows(rows=range(start_row, art_rows)) or start_row!=0:
        break
    start_row = 5-scrollToRow(5, max_scrolls=20)
print()
if saved:
    with open('artifacts.genshinart.json', "wb") as f:
        s = json.dumps(result, ensure_ascii=False)
        f.write(s.encode('utf-8'))
    print('总计扫描了{}个圣遗物，保存了{}个到artifacts.genshinart.json，未保存的则为识别结果无法理解，请到artifacts路径中查看'.format(art_id, saved))
else:
    print('总计扫描了{}个圣遗物，未保存任何圣遗物，未保存的则为识别结果无法理解，请到artifacts路径中查看'.format(art_id, saved))
input('已完成，按回车退出')