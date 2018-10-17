# igxe-c5-buff-csgo-skins-sale-data-catch
Automatically get the csgo skins sale data on igxe.cn and c5game.com and buff.163.com. You can choose the specific skins to get data.

#### 进入py文件设置好自己想监视的csgo皮肤以及筛选规则后，运行脚本，就会输出各大网站中满足筛选条件的皮肤。其中，两个py脚本分别对应不同的饰品网站
### **api_ig_buff.py**使用说明：
- 必备条件：
    - python3环境和requests库
    - 在py文件中补全皮肤在igxe和buff的id（下面会说如何找到皮肤的id），以及所能接受的最高价格和最大磨损
- 皮肤在igxe的id：在igxe中打开某个特定皮肤的销售界面后，链接的末尾即“/product/730”后面的数字就是皮肤的id
- 皮肤在buff的id：在buff中打开某个特定皮肤的销售界面后，链接中的“goods_id=...”就是皮肤的id
- 皮肤的id和后面的价格/磨损的筛选规则需要对应，在list中可输入多个皮肤
- 如果想监视没有磨损值的皮肤如音乐盒或者钥匙，可以在设置规则时将磨损的规则设为一个大于1的数字

### **log_ig_c5.py**使用说明：
- 必备条件：
    - python3，以及requests库，bs4库和lxml库
    - 运行之前需要在代码中开头的部分自定义自己的所需信息，信息的格式和内容已经写在注释中
    - 运行前至少要补全代码开头中ig登陆所需的用户名和密码，即补全"ig_logger"

### 关于这两个脚本
- ```log_ig_c5.py```最后更新于18年3月份，采用的是igxe先模拟登录再用Beautifulsoup爬取信息，C5是直接访问api.需要注意的是igxe现在异地登录有验证
- ```api_ig_buff.py```更新于18年10月份，igxe和buff都用的是api访问，效率更高
- 可以根据自己的需要添加其他功能，比如发电子邮件提醒，每隔一段时间重复检索等