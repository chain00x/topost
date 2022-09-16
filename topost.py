import json
import argparse
parser = argparse.ArgumentParser(description='Testing...') #创建对象
parser.add_argument('i') ##添加单个命令参数
args = parser.parse_args() ##使得参数创建并生效
jdata=args.i

data=json.loads(jdata)
n=0
postdata=''
for i in data:
    n = n+1
    if n < len(data):
        postdata=postdata+(str(i)+"="+str(data[i])+"&").replace('\n','')
    else:
        postdata=postdata+(str(i)+"="+str(data[i])).replace('\n','')
print(postdata.replace(' ','+'))
