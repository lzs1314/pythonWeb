from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, StreamingHttpResponse
from .models import Cateory, Content, GetNum
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils.six import BytesIO
import time
import os, shutil, math
import json
import random
import psutil
import face_recognition
import hashlib
from PIL import Image, ImageDraw
import base64
from django.utils.encoding import escape_uri_path

songs_path = os.path.realpath(os.path.join(__file__, "../../static/mp3/"))
back_path = os.path.realpath(os.path.join(__file__, "../../static/mp3_back/"))

# Create your views here.

# /apis/get_info


def get_info(request):
    """
    用于提供数据
    :param request: HttpRequest
    :return: Json
    """

    if request.method == "GET":
        # 如果是要获取分类列表则加上这个参数  需要提供的内容为: 1ds2ppJu2I9dl1
        cateory_list = request.GET.get("cateory")
        user_list = request.GET.get("users")
        get_access_num = request.GET.get("num")
        get_blog_list = request.GET.get("blog_list")
        get_mp3 = request.GET.get("mp3")
        get_status = request.GET.get("status")

        # 获取分类列表
        if cateory_list is not None and cateory_list == "1ds2ppJu2I9dl1":
            return JsonResponse({
                "status_code": 0,
                "data": [i[0] for i in list(Cateory.objects.values_list("cateory_name"))]
            })

        if user_list is not None and user_list == "2ds2ppJu2I9dl1":
            return JsonResponse({
                "status_code": 0,
                "data": [i[0] for i in list(User.objects.values_list("username"))]
            })

        if get_access_num is not None and get_access_num == "true":
            db = GetNum.objects.get(date=time.strftime("%Y-%m-%d"))
            return JsonResponse({
                "status_code": 0,
                "num": int(db.number)
            })

        if get_blog_list is not None and get_blog_list == "true":
            db = Content.objects.all()
            data = [
                {
                    "title": i.title,
                    "content": i.content,
                    "cateory": i.cateory.cateory_name,
                    "user": i.user.username,
                    "time": i.time
                }
                for i in db]

            return JsonResponse({
                "status_code": 0,
                "data": data
            })
        if get_mp3 is not None:
            data = []
            for i in os.listdir("static/mp3"):
                data.append({"url": f"/apis/static/mp3/{i}",
                             "name": i})
            return JsonResponse({
                "status_code": 0,
                "data": data
            })

        def getMemorystate():
            phymem = psutil.virtual_memory()
            line = "Memory: %5s%% %6s/%s" % (
                phymem.percent,
                str(int(phymem.used / 1024 / 1024)) + "M",
                str(int(phymem.total / 1024 / 1024)) + "M"
            )
            return line

        if get_status is not None:
            data = {}
            data["status_code"] = 0
            data["cpu_utilization"] = int(math.fsum(psutil.cpu_percent(interval=1, percpu=True)) // 4)  # 获得cpu当前使用率
            data["cpu_status"] = max(psutil.cpu_percent(interval=1, percpu=True))  # 获得cpu当前使用率
            data["memory_status"] = int(psutil.virtual_memory().percent)  # 获取当前内存使用情况
            data["disk_status"] = int(psutil.disk_usage("/").percent)

            return JsonResponse(data)

        # =====================================================================================
        return JsonResponse({
            "status_code": 1,
            "error": "not data"
        })


def get_songs(request):
    """
    返回音乐列表
    :param request:
    :return:
    """
    if request.method == "GET":
        # 遍历songs目录, 获取所有歌曲文件名并区分歌曲名与歌手名
        songs_list = os.listdir(songs_path)
        name_or_singer = [song.replace(".mp3", '').split('-') for song in songs_list]

        # 如果目录下存在有两个"-"的文件名则视为强制置顶排序歌曲(表白用的), 下面举个例子
        # 李宗盛 - 我终于失去了你 - 1.mp3
        # 陈奕迅 - 爱情转移 - 2.mp3
        # 王力宏 - 你是我心内的一首歌 - 3.mp3
        list1 = [name for name in name_or_singer if len(name) == 3]
        list2 = [name for name in name_or_singer if len(name) < 3]

        list1.sort(key=lambda x: int(x[2]))

        rspid1 = [name[2].strip() for name in list1]
        name1 = [name[1].strip() for name in list1]
        singer1 = [name[0].strip() for name in list1]
        songs1 = ["-".join(song) + ".mp3" for song in list1]

        rspid2 = [i + len(rspid1) + 1 for i in range(len(list2))]
        name2 = [name[1].strip() for name in list2]
        singer2 = [name[0].strip() for name in list2]
        songs2 = ["-".join(song) + ".mp3" for song in list2]

        # 将置顶歌曲与其他歌曲合并
        rspid = rspid1 + rspid2
        name = name1 + name2
        singer = singer1 + singer2
        songs = songs1 + songs2

        bgp_path = os.path.realpath(os.path.join(__file__, "../../static/image/"))
        bgp_file = os.listdir(bgp_path)
        bgp = []
        for i in range(len(songs)):
            bgp.append(bgp_file[random.randint(0, len(bgp_file) - 1)])

        resp_data = []
        for i in range(len(rspid)):
            resp_data.append({
                "rspid": rspid[i],
                "songs": songs[i],
                "bgp": bgp[i],
                "name": name[i],
                "singer": singer[i]
            })
        resp = {'status_code': 200, 'data': resp_data}
        return JsonResponse(resp)


def download_song(req):
    # do something...
    def file_iterator(file_name, chunk_size=512):
        with open(file_name, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    if req.method == 'GET':
        song_name = req.GET.get('mp3').split('/')[-1]
        the_file_name = os.path.join(songs_path, song_name)
        response = StreamingHttpResponse(file_iterator(the_file_name))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(escape_uri_path(song_name))
        return response




# /apis/add
def add_data(request):
    if request.method == "POST":
        add_blog = request.GET.get("add_data")
        add_access = request.GET.get("access")
        # 添加blog
        if add_blog is not None and add_blog == "1bs2ppJu2I9dl1":
            # 将json转换为python dict格式
            data = json.loads(request.body)
            if data.get("title") is not None and data.get("content") is not None and data.get(
                    "cateory") is not None and data.get("author") is not None:

                # try:
                cateory = Cateory.objects.get(cateory_name=data["cateory"])
                user = User.objects.get(username=data["author"])
                db = Content(title=data["title"], content=data["content"], cateory=cateory, user=user)
                db.save()
                # except:
                #     return JsonResponse({
                #         "status_code": 1,
                #         "error": "save define"
                #     })

                return JsonResponse({
                    "status_code": 0,
                    "data": "success"
                })
            else:
                return JsonResponse({
                    "status_code": 1,
                    "error": "data is vaild"
                })
        # 添加访问数
        if add_access is not None and add_access == "add_access":
            try:
                db = GetNum.objects.get(date=time.strftime("%Y-%m-%d"))
                db.number += 1
                db.save()
                return JsonResponse({
                    "status_code": 0,
                    "data": "first user access"
                })
            except:
                db = GetNum()
                db.number = 1
                db.save()
                return JsonResponse({
                    "status_code": 0,
                    "data": "access success!"
                })

        return JsonResponse({
            "status_code": 1,
            "error": "not done"
        })


# /apis/face  0d62f4e0ccdf47c235e34ba512a882c388f667eae540169c7bfd9a415de303494eea5076f90f21cb2ca0299de4cb3bb2
def checkface(request):
    try:
        files = request.FILES.get("file")
        type_image = files.name.split('.')[-1]
        filename = "./upload/" + hashlib.sha3_384(files.name.encode()).hexdigest() + f".{type_image}"
        with open(filename, "ab+") as fp:
            fp.write(files.read())
        img = BytesIO()
        image = face_recognition.load_image_file(filename)
        locations = face_recognition.face_locations(img=image)
        result_image = Image.fromarray(image)
        for pos in locations:
            d = ImageDraw.Draw(result_image, 'RGBA')
            d.rectangle((pos[3], pos[0], pos[1], pos[2]))
        result_image.save(img, 'png')

        return JsonResponse({
            "status": 0,
            "filename": files.name,
            "face_count": len(locations),
            "resultImg_base": str(base64.b64encode(img.getvalue()).decode())
        })
    except:
        return JsonResponse({
            "status": 1,
            "message": "重试一下吧. 你的照片有问题哦."
        })


class Users:
    @staticmethod
    def get_status(request):
        if request.user.is_authenticated:
            return JsonResponse({
                "status": 0,
                "username": str(request.user),
                "email": str(request.user.email),
            })
        else:
            return JsonResponse({
                "status": 1
            })

    @staticmethod
    def login_user(request):
        if request.method == "POST":
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")
            if username is not None and password is not None:
                islogin = authenticate(request, username=username, password=password)
                if islogin:
                    login(request, islogin)
                    return JsonResponse({
                        "status": 0,
                        "message": "Login Success",
                        "username": username
                    })
                else:
                    return JsonResponse({
                        "status": 1,
                        "message": "登录失败, 请检查用户名或者密码是否输入正确."
                    })
            else:
                return JsonResponse({
                    "status": 2,
                    "message": "参数错误"
                })

    @staticmethod
    def logout_user(request):
        logout(request)
        return JsonResponse({
            "status": 0
        })

    @staticmethod
    def register(request):
        if request.method == "POST":
            data = json.loads(request.body)

            if request.GET.get("select") is not None:
                select_username = data.get("select_username")
                print(select_username)
                try:
                    User.objects.get(username=select_username)
                    return JsonResponse({
                        "status": 0,
                        "is_indb": 1
                    })
                except:
                    return JsonResponse({
                        'status': 0,
                        "is_indb": 0
                    })
            username = data.get("username")
            password = data.get("password")
            email = data.get("email")
            if username is not None and password is not None and email is not None:
                try:
                    user = User.objects.create_user(username=username, password=password, email=email)
                    user.save()
                    login_user = authenticate(request, username=username, password=password)
                    if login_user:
                        login(request, login_user)
                        return JsonResponse({
                            "status": 0,
                            "message": "Register and Login Success"
                        })

                except:
                    return JsonResponse({
                        "status": 2,
                        "message": "注册失败, 该用户名已经存在."
                    })

        else:
            return JsonResponse({
                "status": 1,
                "message": "error method"
            })
