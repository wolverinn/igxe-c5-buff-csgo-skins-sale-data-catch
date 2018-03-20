# igxe-c5-csgo-skins-sale-data-catch
Automatically get the csgo skins sale data on igxe.cn and c5game.com.You can choose the specific skins to get data.
### 实现方法：
- ig需要先登陆才能查询皮肤信息，C5不需要登陆但是页面是动态加载的。虽然用selenium很方便，但是效率很低，所以还是分别采用了模拟登陆和访问API的方式提高抓取效率。
- 可以根据自己的需要添加其他功能，比如发电子邮件，重复检索等
### 使用说明：
- 在运行之前，需要先安装python3.0，以及requests库，bs4库和lxml库
- 运行之前需要在代码中开头的部分自定义自己的所需信息，信息的格式和内容已经写在注释中
- 运行前至少要补全代码开头中ig登陆所需的用户名和密码，否则会查询失败
