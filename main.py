import asyncio

from sanic import Sanic, response
from sanic.request import Request
from sanic.response import text, stream
import os
import time
import subprocess
import uuid
app = Sanic("WebZmap")
@app.get("/webzmap/web/zmap.sh")
async def runZmap(Re: Request):
    fake = """
    #!python3
    # 第一个对应端口, 第二个对应ips
    import os
    function do_zmap(maxs, ip, port):
        os.exec("zmap -N {} -B 10M -q -p{} -o result.txt {}".format(maxs, ip, port))
        tmp = ''
        try:
            with open("result.txt", 'r') as f:
                tmp = f.read()
        except:
            return "result.txt not found"
        return tmp
    do_zmap()
    """
    # 判断是否存在get参数
    try:
        ips = Re.args["ips"][0]
        port = Re.args["port"][0]
        maxs = Re.args["maxs"][0]
        print(Re.args)
        port = int(port)
        maxs = int(maxs)
        if port > 65525 or port < 1 or maxs < 0 or maxs > 10000:
            print(Re.ip)
            with open("hacker.txt", 'a') as f:
                f.write("\n {}, {}".format(Re.ip, Re.args))
            return "result.txt not found"
        test = "qwertyuiopasdfghjklzxcvbnm|!@#$%^&*()_+{}[]':"
        for i in test:
            if i in ips:
                print(Re.ip)
                with open("hacker.txt", 'a') as f:
                    f.write("\n {}, {}".format(Re.ip, Re.args))
                return "result.txt not found"

        async def getOutpu(respond):
            print("zmap -N {} -B 50M -q -p{} {}".format(maxs, port, ips))
            cmd = "zmap -N {} -B 50M -q -p{} {}".format(maxs, port, ips)
            p = await asyncio.subprocess.create_subprocess_shell(cmd,
                                                                 stdout=asyncio.subprocess.PIPE,
                                                                 stderr=asyncio.subprocess.PIPE)
            stdout, stderr = await p.communicate()

            for line in stdout.decode("utf-8").split("\n"):
                r = line.strip()
                with open("/scan/{}.txt".format(port), 'a') as f:
                    f.write(r + "\n")
                await respond.write(r + ":" + str(port) + "\n")

        return stream(getOutpu)
    except Exception as e:
        print(Re.ip)
        with open("hacker.txt", 'a') as f:
            f.write("\n {}, {}".format(Re.ip, Re.args))
        return text(fake)

@app.get("/webzmap/web/setblacklist.sh")
async def setBlackList(Re: Request):
    try:
        key = Re.args["key"][0]
        ip = Re.args["ip"][0]
        if key == "{{HERE}}":
            with open("/etc/zmap/blacklist.conf", 'a') as f:
                f.write(ip + "\n")
            return text("success")
    except:
        pass

@app.get("/webzmap/web/getblacklist.sh")
async def getBlackList(Re: Request):
    try:
        key = Re.args["key"][0]
        if key == "{{HERE}}":
            with open("/etc/zmap/blacklist.conf", 'r') as f:
                return text(f.read())
    except:
        pass

@app.get("/webzmap/web/getresult.sh")
async def getResult(Re: Request):
    try:
        key = Re.args["key"][0]
        port = Re.args["port"][0]
        if key == "{{HERE}}":
            with open("/scan/{}.txt".format(port), 'r') as f:
                return text(f.read())
    except:
        pass

@app.get("/webzmap/web/masscan.sh")
async def runMasscan(Re: Request):
    try:
        ips = Re.args["ips"][0]
        port = Re.args["port"][0]
        if Re.args.get("time") is None:
            times = 10
        else:
            times = Re.args["time"][0]
        print(Re.args)
        port = int(port)
        times = int(times)
        if port > 65525 or port < 1 or times < 0 or times > 120:
            print(Re.ip)
            with open("hacker.txt", 'a') as f:
                f.write("\n {}, {}".format(Re.ip, Re.args))
            return "result.txt not found"
        test = "qwertyuiopasdfghjklzxcvbnm|!@#$%^&*()_+{}[]':"
        for i in test:
            if i in ips:
                print(Re.ip)
                with open("hacker.txt", 'a') as f:
                    f.write("\n {}, {}".format(Re.ip, Re.args))
                return "result.txt not found"

        async def getOutpu(respond):
            uid = str(uuid.uuid4())
            print("masscan -p{} {} --max-rate 1000000 --banners --exclude 255.255.255.255 --source-port 50000-50003 -oJ {}.json".format(port, ips, uid))
            cmd = "masscan -p{} {} --max-rate 1000000 --banners --exclude 255.255.255.255 --source-port 50000-50003 -oJ {}.json".format(port, ips, uid)
            p = await asyncio.subprocess.create_subprocess_shell(cmd,
                                                                 stdout=asyncio.subprocess.PIPE,
                                                                 stderr=asyncio.subprocess.PIPE)
            stdout, stderr = await p.communicate()
            await asyncio.sleep(times)
            p.kill()
            with open("{}.json".format(uid), 'r') as f:
                for i in f.readlines():
                    await respond.write(i)
            subprocess.Popen(["rm", "rf", "{}.json".format(uid)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        return stream(getOutpu)
    except Exception as e:
        print(Re.ip)
        with open("hacker.txt", 'a') as f:
            f.write("\n {}, {}".format(Re.ip, Re.args))
        return text("WTF")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1919)
