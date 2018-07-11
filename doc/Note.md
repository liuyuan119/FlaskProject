# Flask


## 已学知识点
- Flask MTV
- flask-blueprint
- flask-sqlalchemy



## 未学知识点
- flask-script
- flask-migrate
- flask-session
- flask-cache
- flask-debugtoolbar
- 钩子函数
    - AOP
    - django 中的中间件
- flask-mail


### 回顾
- Flask
    - web 微 框架
    - MTV (MVC)
    - wsgi 
    - jinja2
        - 宏定义
        
- 默认一个文件可以实现所有事情    
- 项目开发中会进行分层

- 请求流程
    - browser -> router(在应用上，使用装饰器实现的) -> 视图函数 -> 操作数据库 - > 视图函数 -> Response -> browser
    
### Flask-Script
- 让Flask项目支持命令行参数
- 使用流程
    - 安装 
        - pip install flask-script
    - 初始化
        - manage = Manager(app)
    - 使用
        - 调用参数就ok了
        - h  指定主机
        - p  指定端口
        - d  调试模式
        - r  自动重新加载（服务器自动重启）
        
### 项目拆分
- models
- views
- templates


### Flask-Blueprint
- 蓝图
    - 美好的向往，规划
- 规划了请求
- 使用流程
    - 安装
        - pip install flask-blueprint
    - 初始化
        - 在 app 注册蓝图
    - 使用蓝图注册路由
        - @blue.route('xxx'')
        
        
### Flask-SQLAlchemy
- ORM 框架
- 定义models
- 封装数据库的操作


### Flask-Migrate
- 迁移库
- 实现数据库迁移
- 使用流程
    - 安装
        - pip install flask-migrate
    - 初始化
        - 创建一个migrate对象
        - 需要和models关联，SQLAlchemy对象进行关联
        - 需要和app关联
        - 和Flask-Script结合使用
            - 在manager对象上添加指令
            - manager.add_command('db', MigrateCommand)
    - 使用
        - python manage.py db xxx
            - init  首次使用必须调用 init
            - migrate   生成迁移文件
            - upgrade   升级，执行迁移文件
            - downgrade 降级，执行迁移文件
            - 升级和降级都是迁移文件中的一个函数


#### ext.py
- extension 扩展
- 创建一个单独的文件，统一管理全局的各种插件


### 项目结构
- App
    - __init__
    - settings.py 
    - ext
        - 统一管理第三方包
        - ORM, SQLAlchemy 对象
        - 衍生models
    - views
- doc
- migrations
- manage.py
- requeirements.txt
- venv
    - 虚拟环境放在工程根目录
    - 全局虚拟环境
 
    
#### Flask 四大内置对象
- request
- session
    - 内存中
    - 数据库
    - 缓存中（Redis）
    - 文件中
    - cookie
- g
    - 全局对象
    - 传递数据
    - 跨函数传递数据
- config
    - app.config
    - 模板中直接使用 config
    - 在app需要获取到app对象 再获取config
        - 获取运行的app  
        - current_app


#### Flask-session
- 提供Flask中的session处理策略
- 使用流程
    - 安装
        - pip install flask-session
    - 初始化
        - 指定SESSION_TYPE
        
    - 使用
        - 和原生session一样
        
#### Flask-Caching 
- 从Flask-Cache中剽窃的
- 使用流程
    - 安装
        - pip install flask-caching
    - 初始化
        - 使用App构建cache对象
        - 指定 config 
            - CACHE_TYPE,  redis
    - 使用
        - @cache.cached(timeout=50)
        
- cache 还有一些可操作函数
    - add
    - set
        - set_many
    - get
        - get_many
    - delete
        - delete_many
    - clear  
        
     
#### 项目体系
- 如果项目需要添加额外扩展库
    - 直接在 ext中添加
    - 和路由相关的，独立出来
        - 蓝图
        - restful api
- 实现功能
    - 建模（定义数据）
    - 路由和视图函数
        - 蓝图写法
            - 每个功能都创建自己的一个蓝图
            - 在app上注册蓝图
            - 使用蓝图注册自己的功能
        - 使用 rest api
            - 创建自己的resource
            - 在api上注册resource
    - 返回
        - 最终都是Response
        - RESTAPI中返回字典会自动被转换成JSON