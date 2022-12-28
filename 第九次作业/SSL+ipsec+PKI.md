## 实验前提

本次实验都是基于win11环境以及同一局域网下的操作

主要参考群内叶臻强师兄的文档报告进行学习

服务器端ip

![image-20221224125304649](img/image-20221224125304649.png)

客户端ip

![image-20221224125249922](img/image-20221224125249922.png)

特点：操作方便，对于没有虚拟机条件的同学比较友好

## SSL

### 配置服务器

打开控制面板 -->程序和功能

![image-20221224125842041](img/image-20221224125842041.png)

启动或关闭Windows功能

![image-20221224125900617](img/image-20221224125900617.png)

找到Internet Infomation Services将原本没有勾选上的全部选上

![image-20221224130014160](img/image-20221224130014160-16718580144361.png)

进入如下界面，等待即可

![image-20221224130028810](img/image-20221224130028810.png)

搜索Internet Information Services (IIS)管理器打开

![image-20221224130350890](img/image-20221224130350890.png)

界面如下

![image-20221224130414457](img/image-20221224130414457.png)

右键网站-->添加网站

![image-20221224130638738](img/image-20221224130638738.png)



进入如下配置界面，物理路径可以任意，这里我放在作业目录下，IP地址选择本机局域网ip

![image-20221224131514522](img/image-20221224131514522.png)

在上述文件夹下创建一个基本的index.html可访问文件

![image-20221224134144305](img/image-20221224134144305.png)

修改index.html内容

![image-20221224135144987](img/image-20221224135144987.png)

继续配置网站权限，右键新建网站-->编辑权限

选择安全选项卡，点击编辑

![image-20221224134318323](img/image-20221224134318323.png)

添加Everyone对象

![image-20221224134437021](img/image-20221224134437021.png)

授予权限

![image-20221224134506398](img/image-20221224134506398.png)

测试：

使用本地局域网ip进入网址，可以访问到刚刚创建的index.html，说明网站配置成功

![image-20221224135245909](img/image-20221224135245909.png)

客户端也可以正常访问

![image-20221224140153392](img/image-20221224140153392.png)

### 未启用SSL情况下抓包

打开Wireshark，点击WLAN

![image-20221224135431422](img/image-20221224135431422.png)

输入客户端ip，设置过滤器

![image-20221224135556853](img/image-20221224135556853.png)

客户端访问服务器192.168.43.63,服务端使用wireshark抓包

![image-20221224143952637](img/image-20221224143952637.png)

如下，HTTP 200 OK的包中，可以发现没有使用SSL的情况下网络间的数据是赤裸的

### 为网站配置SSL证书

回到网站所在的根目录，找到服务器证书-->创建自签名证书

![image-20221224192022184](img/image-20221224192022184.png)

启动ssl服务

![image-20221224192737505](img/image-20221224192737505.png)

修改web.config文件

![image-20221224192708603](img/image-20221224192708603.png)

重新添加网站，选择https类型，添加刚刚创建的证书，将端口号设置为81

![image-20221224192617448](img/image-20221224192617448.png)



重新抓包

![image-20221224192810931](img/image-20221224192810931.png)

可以看到在https协议下，使用自签名证书则只会显示TCP握手协议，所以SSL证书必不可缺

## IPSEC

### Windows配置

- win+r打开命令板输入mmc打开控制台

- 点击文件，选择添加/删除管理单元

![image-20221224193211693](img/image-20221224193211693.png)

- 添加IP安全策略管理

![image-20221224193348308](img/image-20221224193348308.png)

- 右键创建IP安全策略

![image-20221224193826875](img/image-20221224193826875.png)

![image-20221224193855287](img/image-20221224193855287.png)

- 双击打开属性窗口

![image-20221224193947089](img/image-20221224193947089.png)

- 添加

![image-20221224194015810](img/image-20221224194015810.png)

点击下一步，不指定隧道，下一步，所有网络，下一步，添加ip筛选器

![image-20221224194114319](img/image-20221224194114319.png)

![image-20221224194218480](img/image-20221224194218480.png)

点击确定返回，勾选ip筛选器

![image-20221224194609258](img/image-20221224194609258.png)

进入下一页，点击添加筛选器操作

![image-20221224194645762](img/image-20221224194645762.png)

选择协商安全，下一步增加身份验证方法，输入3120005043，并进行指派

![image-20221224194757377](img/image-20221224194757377.png)

检测网络

![image-20221224195527551](img/image-20221224195527551.png)

网络连通

抓包

![image-20221224195629015](img/image-20221224195629015.png)

- 使用ESP加密且认证

![image-20221224195911598](img/image-20221224195911598.png)

![image-20221224195948568](img/image-20221224195948568.png)

重新访问

![image-20221224200041168](img/image-20221224200041168.png)

- 采用ESP，只认证

![image-20221224200135322](img/image-20221224200135322.png)

![image-20221224200209614](img/image-20221224200209614.png)

## PKI

- 安装
- 配置环境变量
- 测试安装成功

![image-20221224171231364](img/image-20221224171231364.png)

列出可用的ECC曲线`openssl ecparam -list_curves`

![image-20221224174933252](img/image-20221224174933252.png)

我使用prime256v1生成ECC秘钥对，使用ECC key生成CA证书

首先生成CA ECC密钥 

`openssl ecparam -out private/ec-cakey.pem -name prime256v1 -genkey`

`openssl ecparam -in private/ec-cakey.pem -text -noout`

![image-20221224175036669](img/image-20221224175036669.png)

然后生成CA证书

`openssl req -new -x509 -days 3650 -config openssl.cnf -extensions v3_ca -key private/ec-cakey.pem -out cert/ec-cacert.pem`

![image-20221224175128721](img/image-20221224175128721.png)

验证CA证书内容及使用的签名算法

`openssl x509 -noout -text -in cert/ec-cacert.pem`

![image-20221224175200693](img/image-20221224175200693.png)

验证CA证书

- 使用私钥验证CA证书
- 从私钥导出公钥

![image-20221224175239301](img/image-20221224175239301.png)

可以看到两种方式的公钥相同

#### 使用CA私钥和证书签发服务端证书

- 生成ECC私钥`openssl ecparam -out server.key -name prime256v1 -genkey`
- 生成CSR请求`openssl req -new -key server.key -out server.csr -sha256`

![image-20221224175330236](img/image-20221224175330236.png)

- 使用ECC私钥及CA证书，对server.csr签名，生成服务端证书

`openssl ca -keyfile ../private/ec-cakey.pem -cert ../cert/ec-cacert.pem -in server.csr -out server.crt -config ../openssl.cnf`

![image-20221224181617566](img/image-20221224181617566.png)

验证证书是否有效时使用CA证书

![image-20221224181631211](img/image-20221224181631211.png)

验证index.txt

![image-20221224181711403](img/image-20221224181711403.png)

