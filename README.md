## sychronize-data 生产api的json数据sql脚本

### 项目分层
```
src >
    com >
        config    # 配置(pool_id、文件路径、文件名、sql模板等)
        dao       # 请求并解析json数据并整理到list对象中
        model     # 对象模型
        request   # 请求网络json数据接口
        service   # 处理list对象关系与业务逻辑
        file      # 输出sqlList到文件
        controller# 控制器，提供各种实现业务的功能
        
    main          # 主运行程序，运行并执行功能
```

### 运行教程
1.修改配置文件(src/com/config/config.py)
2.运行，python src/main.py
2.测试，python src/test.py

### Bug
1.67版本.从json获取参数rrs时失败，@权威区下没有rrs字段
2.tenant_id = noauth-project(done)
3.uuid去掉-(done)
4.出掉字段中的u'与[](done)
5.对和关键字相同的字段添加`符号