## sychronize-data 生产api的json数据sql脚本

### 项目分层
```
src >
    com >
        config    # 配置pool_id、文件路径、文件名、sql模板等(done)
        dao       # 请求并解析json数据并整理到list对象中(done)
        model     # 对象模型(done)
        request   # 请求网络json数据接口(done)
        driver    # 请求zdnsjson数据接口(done)
        service   # 处理list对象关系与业务逻辑(done)
        util      # 输出sqlList到文件(done)
        controller# 控制器，提供各种实现业务的功能(done)
        view	  # 界面(wait)
        
    main          # 主运行程序，运行生产sql (done)
    mainWithGUI   # 主运行程序			 (wait)
    test          # windows下测试程序 	 (done)
    test_get_zdns # 测试zdns网络是否通	    (done)
    
```

### 运行教程
1.修改配置文件(src/com/config/config.py)
2.运行，python src/main.py
2.测试，python src/test.py

### Bug
1.tenant_id = noauth-project(done)
2.uuid去掉-(done)
3.出掉字段中的u'与[](done)
4.对和关键字相同的字段添加`符号(done)

