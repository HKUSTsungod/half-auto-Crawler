#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import lxml
import time
import random
import re
import m3u8
import ffmpeg


index = 1  # modify this number to start from different video (for conveniently dividing download into parts)

class VideoCrawler():
    def __init__(self):
        self.down_path = r"/Users/sungod/Downloads/process"
        self.final_path = r"/Users/sungod/Downloads/final"
        self.m3u8_path = r"/Users/sungod/Downloads/m3u8"
        try:
            self.name = re.findall(r'/[A-Za-z]*-[0-9]*', self.url)[0][1:]
        except:
            self.name = "uncensord"
        self.headers = {
            'Connection': 'Keep-Alive',
            'Accept': 'text/html, application/xhtml+xml, */*',
            'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
            'User-Agent':'Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-m2 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.5.506 UWS/2.10.1.22 Mobile Safari/537.36'
        }

    def get_m3u8_list(self, index):
        list = []
        dir = os.listdir(self.m3u8_path)
        dir.sort()
        i = 1
        for f in dir:
            if str(f)[-1] == '8':
                if i < index:
                    i = i + 1
                    continue
                else:
                    list.append(self.m3u8_path + "/" + str(f))
        return list

    def get_uri_from_m3u8(self, file_name):
        print("正在解析真实下载地址..." + str(file_name))
        m3u8Obj = m3u8.load(file_name)
        print("解析完成.")
        return m3u8Obj.segments

    def get_ts_from_segment(self, segment, k):
        os.chdir(self.down_path)
        k_str = ''
        if k < 10:
            k_str = '00' + str(k)
        elif k < 100:
            k_str = '0' + str(k)
        else:
            k_str = str(k)

        start_time = time.time()
        i = 1  # count
        for key in segment:
            try:
                resp = requests.get("https://media.wanmen.org/" + key.uri, headers=self.headers)
            except Exception as e:
                print(e)
                return
            if i < 10:
                name = ('clip00%d.ts' % i)
            elif i > 100:
                name = ('clip%d.ts' % i)
            else:
                name = ('clip0%d.ts' % i)
            with open(name, 'wb') as f:
                f.write(resp.content)
                print('正在下载clip%d' % i)
            i = i + 1

        print("下载完成！总共耗时 %d s" % (time.time() - start_time))
        print("接下来进行合并……")
        os.chdir(self.down_path)
        os.system('cat *.ts > ../final/video.ts')
        os.chdir(self.final_path)
        cmd = 'ffmpeg -i video.ts -c copy %s.mp4' % k_str
        os.system(cmd)
        print("合并完成，请您欣赏！")
        files = os.listdir(self.down_path)
        for filena in files:
            del_file = self.down_path + "/" + filena
            os.remove(del_file)
        os.remove(self.final_path + '/video.ts')
        print("碎片文件已经删除完成")

    def run(self):
        print("Start!")

        os.chdir(self.down_path)
        list = self.get_m3u8_list(index)
        print('list length: ' + str(len(list)))

        k = index
        for obj in list:
            self.get_ts_from_segment(self.get_uri_from_m3u8(obj), k)
            print('第' + str(k) + "个视频解析成功")
            k = k + 1





if __name__=='__main__':
    crawler = VideoCrawler()
    crawler.run()