import requests  
import os  
import json  
  
# 接口的URL  
url = 'https://git.acwing.com/iduoduo/orange/-/raw/main/jsm.json'  # 请替换为您的实际接口URL  
  
# 发送HTTP GET请求  
response = requests.get(url)  
  
# 检查请求是否成功  
if response.status_code == 200:  
    # 解析JSON数据  
    data = response.json()  
      
    # 假设JSON响应包含一个名为'files'的列表，每个元素都是一个包含文件URL的字典  
    files = data.get('files', [])  
      
    # 遍历文件列表  
    for file_info in files:  
        file_url = file_info.get('url')  # 获取文件URL  
        file_name = os.path.basename(file_url)  # 从URL中提取文件名（可能需要根据实际情况调整）  
          
        # 发送HTTP GET请求下载文件  
        with requests.get(file_url, stream=True) as r:  
            # 检查下载请求是否成功  
            if r.status_code == 200:  
                # 指定保存文件的路径（可以根据需要修改）  
                save_path = 'downloaded_files/'  
                os.makedirs(save_path, exist_ok=True)  # 确保目录存在  
                full_file_path = os.path.join(save_path, file_name)  
                  
                # 以二进制模式打开文件并写入数据  
                with open(full_file_path, 'wb') as f:  
                    for chunk in r.iter_content(chunk_size=8192):  
                        f.write(chunk)  
                  
                print(f"文件 {file_name} 已成功保存到 {full_file_path}")  
            else:  
                # 下载请求失败，打印错误信息  
                print(f"下载文件 {file_name} 失败，状态码：{r.status_code}")  
else:  
    # 初始请求失败，打印错误信息  
.json    print(f"请求失败，状态码：{response.status_code}，错误信息：{response.text}")