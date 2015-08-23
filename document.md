# EMS设计文档

## 功能需求
- 提供记账功能
- 可自动将账户借记关系简化
- 提供一些数据统计功能

## 数据库设计
- 用户表格

| 名称 | 类型 | 说明 |备注|
| --- | --- | --- | --- |
| user_id | int |用户id |主键,自增|
| name | varchar(20) | 用户名，登录使用 | |
| real_name | varchar(20) | 真实姓名 | |
| password | char(20) | 密码 | 6-20位可打印acsii字符 |
| email | varchar(320) | 邮箱地址 | 备用|
| group | varchar(20) | 组群 | 备用,目前所有用户的组群都为default |


- 事件表格

| 名称 | 类型 | 说明 |备注|
| --- | --- | --- | --- |
|event_id| int|事件id|主键,自增|
|creator|varchar(20)|创建人真实姓名||
|event_desc|varchar(40)|事件描述||
|gmt_create|date|创建时间||
|event_status|int|状态:0(新建),1(已确认),2(已删除)||


- 借记关系表格
 
| 名称 | 类型 | 说明 |备注|
| --- | --- | --- | --- |
|lending_id| int|借记关系id|主键,自增|
|value|int|金钱，单位：元||
|from_user|varchar(20)|出借方真实姓名||
|to_user|varchar(20)|入借方真实姓名||
|event_id|int|事件id||
|gmt_create|date|创建时间||
|lendings_status|int|借记关系状态,0(新建),1(已确认),2(已拒绝),3(已完结),4(已取消)| | 


## 接口设计

content-type均为application/json

### 用户信息接口
#### 查询用户信息
- GET: /user/query
 
- args

 |参数|说明|备注|
 |---|----|----|
 |id |用户id|必选|
- return
 
 ```json
  {
    "code": 0,
    "desc": "ok",
    "result": {
      "email": "@",
      "user_id": 1,
      "name": "zstbsqx",
      "real_name":"程季",
      "group": "104B,104,计24"
    }
  }
 ```

#### 获取当前处于同一组群的用户列表
- GET: /user/list
 
- args

 |参数|说明|备注|
 |---|----|----|
 |group ||必选|
- return
 
 ```json
  {
    "code": 0,
    "desc": "ok",
    "result": [
        {
            "email": "@",
            "user_id": 1,
            "name": "zstbsqx",
            "real_name":"程季",
            "group": "default"
        },
        {
            "email": "@",
            "user_id": 2,
            "name": "winton",
            "real_name":"罗富文",
            "group": "default"
        },
        {
            "email": "@",
            "user_id": 3,
            "name": "zhoulinjun1994",
            "real_name":"周琳钧",
            "group": "default"
        }
    ]
  }
 ```

#### 用户注册
- POST: /user/create
- args

 |参数|说明|备注|
 |----|----|----|
 |email|电子邮件地址|必选|
 |name|用户名|必选|
 |real_name|真实姓名|必选|
 |password|密码|必选|
- return

 ```json
    {
        "code": 0,
        "desc": "ok"
    }
 ```

#### 用户登录
- POST: /user/login
- args

 |参数|说明|备注|
 |----|----|----|
 |name|用户名|必选|
 |password|密码|必选|
- return

 ```json
    {
        "code": 0,
        "desc": "ok"
    }
 ```
 
 #### 用户退出登录
- POST: /user/logout
- args
 无
- return

 ```json
    {
        "code": 0,
        "desc": "ok"
    }
 ```

### 事件信息
#### 获取事件列表
- GET: /event/list
- args

 |参数|说明|备注|
 |----|----|----|
 |page|页号|默认：0|
 |page_size|每页显示的条数|默认:25|
- return

 ```json
    {
        "code": 0,
        "desc": "ok",
        "result":[
            {
                "event_id":10834,
                "creator": "周琳钧",
                "event_desc": "电影《捉妖记》",
                "gmt_create": "2015-08-12 20:26:31",
                "event_status":0
            },
            {
                "event_id":10824,
                "creator": "罗富文",
                "event_desc": "豪尚豪牛排",
                "gmt_create": "2015-08-12 20:26:31",
                "event_status":0
            },
            {
                "event_id":834,
                "creator": "程季",
                "event_desc": "日本回转寿司",
                "gmt_create": "2015-08-12 20:26:31",
                "event_status":0
            }
        ]
    }
```

#### 获取事件详情
- GET: /event/query
- args

 |参数|说明|备注|
 |----|----|----|
 |event_id||必选|
- return

 ```json
    {
        "code": 0,
        "desc": "ok",
        "result":{
            "event_id":10834,
            "creator": "周琳钧",
            "creator_id": 12,
            "event_desc": "东方饺子王",
            "gmt_create": "2015-08-12 20:26:31",
            "event_status": 0,
            "lendings": [
                {
                    "lending_id": 3,
                    "lending_status": 0,
                    "value": "67",
                    "from_user": "周琳钧",
                    "to_user": "罗富文",
                    "event_id": 10834,
                    "gmt_create": "2015-08-12 20:26:31"
                },
                {
                    "lending_id": 4,
                    "lending_status": 0,
                    "value": "67",
                    "from_user":"周琳钧",
                    "to_user": "程季",
                    "event_id": 10834,
                    "gmt_create": "2015-08-12 20:26:31"
                }
            ]
        },
    }
```


#### 创建事件
- POST: /event/creator
- args

 |参数|说明|备注|
 |----|----|----|
 |event_desc|事件描述|必选|
 |lendings|{["from_user":"userA","to_user":"userB","value":20],["from_user":"userA","to_user":"userC","value":30]}|格式为json的字符串|
- return

 ```json
    {
        "code": 0,
        "desc": "ok"
    }
```

### 借记关系接口
#### 查询借记关系
- GET: /lending/query
- args

 |参数|说明|备注|
 |----|----|----|
 |lending_id||必选|
- return

 ```json
    {
        "code": 0,
        "desc": "ok",
        "result":{
            {
                "lending_id": 3,
                "lending_status": 0,
                "value": "67",
                "from_user": "周琳钧",
                "to_user": "罗富文",
                "event_id": 10834,
                "gmt_create": "2015-08-12 20:26:31"
            }
        },
    }
```

#### 更新借记关系
- POST: /lending/update
- args

 |参数|说明|备注|
 |----|----|----|
 |lending_id||必选|
 |lending_status|不为空则更新该字段|可选|
 |value|不为空则更新该字段|可选|
- return

 ```json
    {
        "code": 0,
        "desc": "ok",
    }
```


## 页面设计
- 主页：包含记事，还钱等快捷按钮
- 事件页面：事件列表显示，按时间排列，每一则事件显示名称，和时间
- 关系页面：列表，显示用户，以及与这个用户的汇总借记关系，选择某个关系进入，然后还钱
- 登录页面：使用用户名和密码登录
- 注册页面：填写用户名，真实姓名，密码，邮箱
