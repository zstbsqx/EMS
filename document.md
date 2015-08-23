# EMS设计文档

## 功能需求
- 提供记账功能
- 可自动将账户借记关系简化
- 提供一些数据统计功能

## 数据库设计
- 用户表格

| Field | Type | Null | Key | Default | Extra |
| --- | --- | :---: | :---: | --- | :---: |
| id | int | no | PRI | | auto increment |
| name | varchar(20) | no | | | |
| password | char(32) | no | | | |
| email | varchar(320) | yes | | | |

- 事件表格

| Field | Type | Null | Key | Default | Extra |
| --- | --- | :---: | :---: | --- | :---: |
| id | int | no | PRI | | auto incrment |
| owner | int | no | | | foreign key |
| comment | test | | | | |
| date | date | | | Date() | |
| status | int(3) | | | 0 | |

 status为借钱状态
  0: 新建
  1: 已确认
  2: 已删除
  3: 备用

- 借记关系表格

| Field | Type | Null | Key | Default | Extra |
| --- | --- | :---: | :---: | --- | :---: |
| value | int | no | | | |
| fromuser | int | no | MUL | | foreign key |
| touser | int | no | MUL | | foreign key |
| event | int | no | MUL | | foreign key | 

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
      "id": 1,
      "name": "程季"
    }
  }
 ```

#### 用户注册
- POST: /user/create
- args

 |参数|说明|备注|
 |----|----|----|
 |email|电子邮件地址，登录用|必选|
 |name|用户名|必选|
 |password|密码|必选|
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
                "id":10834,
                "owner": "周琳钧",
                "comment": "电影《捉妖记》",
                "date": "2015-08-12 20:26:31",
                "status":0
            },
            {
                "id":10034,
                "owner": "罗富文",
                "comment": "豪尚豪牛排",
                "date": "2015-08-12 22:26:31",
                "status": 1
            },
            {
                "id":834,
                "owner": "程季",
                "comment": "日本回转寿司",
                "date": "2015-07-12 20:26:31",
                "status": 1
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
            "id":10834,
            "owner": "周琳钧",
            "comment": "东方饺子",
            "date": "2015-08-12 20:26:31",
            "status":0,
            lendings: [
                {
                    "id": 3,
                    "fromuser": "周琳钧",
                    "touser": "罗富文",
                    "value": "67"
                },
                {
                    "id": 4,
                    "fromuser": "周琳钧",
                    "touser": "程季",
                    "value": "67"
                }
            ]
        },
    }
```



## 页面设计
- 主页：包含记事，还钱等快捷按钮
- 事件页面：事件列表显示，按时间排列，每一则事件显示名称，和时间
- 关系页面：列表，显示用户，以及与这个用户的汇总借记关系，选择某个关系进入，然后还钱
- 登录页面：使用用户名和密码登录
- 注册页面：填写用户名，真实姓名，密码，邮箱
