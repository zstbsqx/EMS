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

- [已废弃]好友关系表格

| Field | Type | Null | Key | Default | Extra |
| --- | --- | :---: | :---: | --- | :---: |
| user | varchar(20) | no | MUL | | foreign key |
| friend | varchar(20) | no | MUL | | foreign key |
| lend | int | no | | 0 | |

 lend > 0 : friend欠user钱
 lend < 0 : 相反

- 事件表格

| Field | Type | Null | Key | Default | Extra |
| --- | --- | :---: | :---: | --- | :---: |
| id | int | no | PRI | | auto incrment |
| owner | int | no | | | foreign key |
| comment | test | | | | |
| date | date | | | Date() | |
| status | int(3) | | | 0 | |

 status为借钱状态
  0: 未确认 
  1: 已确认
  2: 已拒绝
  3: 备用

- 借记关系表格

| Field | Type | Null | Key | Default | Extra |
| --- | --- | :---: | :---: | --- | :---: |
| value | int | no | | | |
| from | int | no | MUL | | foreign key |
| to | int | no | MUL | | foreign key |
| event | int | no | MUL | | foreign key | 

## 接口设计

content-type均为application/json

unsafe的接口返回的信息均为
```
{
    int:code,
    str:desc, 
    int:user
}
```

### 用户信息
  /api/users/\<int:id\>

  + get

  根据query中的id找出相关用户信息，返回
  ```
  {
    int:id,
    str:name,
    str:email
  }
  ```

  + post

  body所含信息为
  ```
  {
    str:name,
    (hashed)str:password,
    str:email
  }
  ```

  + patch

  更新信息，为了兼容这部分也可以放到post里
  ```
  {
    int:id,
    [changed fields]
  }
  ```


  + delete

  只有本人可以删除
  ```
  {
    int:id
  }
  ```

### 事件信息
  /api/event/
  + get

  如果提供了id就直接查询id，否则如果提供了userid，就找出这个user相关的时间，按时间降序排序
  ```
  {
    int:id,
    int:userid
  }
  ```

  + post

  ```
  {
    int:owner,
    str:comment,
    date:date,
    int:status,
    list:lends:[{
      int:to,
      int:value (positive or negative)
    }]
  }
  ```

  + patch

  更新信息，为了兼容这部分也可以放到post里
  ```
  {
    int:id,
    [changed fields]
  }
  ```

  + delete
  
  根据id删除事件，只有owner可以删除
  ```
  {
    int:id
  }
  ```

## 页面设计

