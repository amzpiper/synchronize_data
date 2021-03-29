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
1.修改配置文件(src\com\config\config.py)
2.进入src目录，python main.py

### Bug
1.67.创建模型时从json获取参数rrs时，@权威区下没有rrs字段
2.tenant_id = noauth-project
3.uuid去掉-
4.出掉字段中的u'与[]
