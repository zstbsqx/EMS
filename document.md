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

- 好友关系表格

| Field | Type | Null | Key | Default | Extra |
| --- | --- | :---: | :---: | --- | :---: |
| user | varchar(20) | no | MUL | | foreign key |
| friend | varchar(20) | no | MUL | | foreign key |

- 事件表格

| Field | Type | Null | Key | Default | Extra |
| --- | --- | :---: | :---: | --- | :---: |
| id | int | no | PRI | | auto incrment |
| comment | test | | | | |


- 借记关系表格

| Field | Type | Null | Key | Default | Extra |
| --- | --- | :---: | :---: | --- | :---: |
| value | int | no | | | |
| from | int | no | MUL | | foreign key |
| to | int | no | MUL | | foreign key |
| event | int | no | MUL | | foreign key | 

## 接口设计

## 页面设计

