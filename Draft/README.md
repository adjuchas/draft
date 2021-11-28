# 东莞城市学院 绿洲征稿平台

------

## Oasis-draft-platform

> 东莞城市学院 绿洲征稿平台

### 前端技术

* Vue3.x
* Element-ui
* axios

### 后端技术

#### 技术选型

| 技术   | 版本 | 描述 |
| ------ | ---- | ---- |
| Python | 3.6 | 后端语言 |
| Django | 3.2.7 | 框架 |
| MySQL  | 8.0.25 | 关系型数据库 |
| Redis  | 3.2.12 | Key-Value数据库 |

------

### 数据库设计

| 表名 | 说明 |
| ---- | ---- |
| stu_info | 存储登入的学生个人信息 |
| stu_upload | 存储学生的上传记录 |
| admin215 | 存储管理员信息 |

##### stu_info： 

| 序号 | 名称 | 数据类型 | 允许空值 | 主键 | 说明 |
| ---- | ---- | -------- | -------- | ---- | ---- |
| 1 | yb_stuid | varchar(12) | N | PK | 学生学号 |
| 2 | yb_realname | varchar(10) | N |  | 学生姓名 |
| 3 | yb_id | int | N |  | 易班id |
| 4 | create_time | datetime(6) | N |  | 首次登入时间 |
| 5 | yb_classname | varchar(20) | Y |  | 学生班级信息 |
| 6 | yb_collegename | varchar(15) | Y | | 学生二级学院信息 |



##### stu_upload：

| 序号 | 名称 | 数据类型 | 允许空值 | 主键 | 说明 |
| ---- | ---- | -------- | -------- | ---- | ---- |
| 1 | stuid | varchar(12) | N |  | 学生学号 |
| 2 | recode_id | int | N | PK | 记录ID |
| 3 | upload_name | varchar(20) | N |  | 学生上传的作品名称 |
| 4 | upload_type | int | N |  | 上传作品的类型 |
| 5 | upload_state | varchar(10) | Y |  | 作品状态 |
| 6 | create_time | datetime(6) | N | | 上传作品的时间 |



##### admin215：

| 序号 | 名称 | 数据类型 | 允许空值 | 主键 | 说明 |
| ---- | ---- | -------- | -------- | ---- | ---- |
| 1 | admin_id | varchar(12) | N | PK | 管理员账号 |
| 2 | yb_realname | varchar(10) | N |  | 管理员姓名 |

-----

### 测试接口

##### 用户端

##### 1.回调接口

> 请求URL:'https://csxy-yiban.cn/api/app215/oauth/app215/'
> 
> 请求方法:'GET',

参数：

| 参数名 | 类型   | 必选 | 说明                  |
| ------ | ------ | ---- | --------------------- |
| code   | string | 是   | 易班授权码            |
| state  | string | 是   | 前端算法加密生成的uid |

返回示例：

* 管理员重定向至管理端

  > [绿洲征稿管理平台 ](https://csxy-yiban.cn/pages/215_admin/)

* 非管理员重定向至用户端

  > [易班绿洲 线上征稿平台 ](https://csxy-yiban.cn/pages/215/)

##### 2.获取access_token

> 请求URL：https://csxy-yiban.cn/api/app215/oauth/get_accesstoken/
>
> 请求方法：'GET'

参数：

| 参数名 | 类型   | 必须 | 描述                        |
| ------ | ------ | ---- | --------------------------- |
| uid    | string | 是   | 前端后存在localstorage的uid |

返回示例：

```JSON
{
    "message": "success",
    "access_token": "modelToken"
}
```

##### 3.获取用户信息

> 请求URL：https://csxy-yiban.cn/api/app215/oauth/get_info/
>
> 请求方法：'GET'

参数：

| 参数名       | 类型   | 必须 | 描述     |
| ------------ | ------ | ---- | -------- |
| access_token | string | 是   | 用户密钥 |

返回示例：

```JSON
{
    "message": "success",
    "info": {
        "stuid": "202035020128",
        "name": "马祖贤",
        "yb_id": "39446203",
        "collage_name": "计算机与信息学院",
        "yb_classname": "2020级软件工程1班"
    }
}
```

##### 4.获取用户提交记录

> 请求URL：https://csxy-yiban.cn/api/app215/admin_215/selectall/
>
> 请求方法：'GET'

参数：

| 参数名       | 类型   | 必须 | 描述     |
| ------------ | ------ | ---- | -------- |
| access_token | string | 是   | 用户密钥 |

返回示例：

```JSON
{
    "message": "success",
    "all_recode": [
         {
            "stuid": "202035020128",
            "recode_id": xxx,
            "upload_name": "xxxxx.docx",
            "upload_type": "青春风采,诗歌作品",
            "upload_state": "待审核",
            "create_time": "2021-11-23 14:46:29"
        }
    ]
}
```

##### 5.用户上传作品

> 请求URL：https://csxy-yiban.cn/api/app215/stu/upload_file/
>
> 请求方法：'POST'

参数：

| 参数名       | 类型   | 必须 | 描述               |
| ------------ | ------ | ---- | ------------------ |
| access_token | string | 是   | 用户密钥           |
| file         | string | 是   | 用户上传的文件     |
| file_type    | string | 是   | 上传的文件主题类型 |

返回示例：

```JSON
{
    "message": "success"
}
```

##### 6.用户下载作品

> 请求URL：https://csxy-yiban.cn/api/app215/stu/download/
>
> 请求方法：'POST'

参数：

| 参数名       | 类型   | 必须 | 描述     |
| ------------ | ------ | ---- | -------- |
| access_token | string | 是   | 用户密钥 |
| recoedes     | Array  | 是   | 作品ID   |

返回示例：

```JSON
{
    "message": "success"
}
```

##### 7.用户登出

> 请求URL：https://csxy-yiban.cn/api/app215/oauth/logout/
>
> 请求方法：'POST'

参数：

| 参数名       | 类型   | 必须 | 描述      |
| ------------ | ------ | ---- | --------- |
| access_token | string | 是   | 用户密钥  |
| uid          | string | 是   | 生成的uid |

返回示例：

```JSON
{
    "message": "success"
}
```

##### 管理端

##### 1.获取所有提交记录

> 请求URL：https://csxy-yiban.cn/api/app215/admin_215/selectall/
>
> 请求方法：'GET'

参数：

| 参数名       | 类型   | 必须 | 描述     |
| ------------ | ------ | ---- | -------- |
| access_token | string | 是   | 用户密钥 |

返回示例：

```JSON
{
    "message": "success",
    "recodes": [
        {
            "stuid": "202035020128",
            "recode_id": 1,
            "upload_name": "xxxxx.docx",
            "upload_type": "时代印记,诗歌作品",
            "upload_state": "待审核",
            "create_time": "2021-11-23 14:25:04"
        },
        {
            "stuid": "202035020128",
            "recode_id": 2,
            "upload_name": "xxxxx.docx",
            "upload_type": "青春风采,诗歌作品",
            "upload_state": "待审核",
            "create_time": "2021-11-23 14:46:29"
        }
    ]
}
```

##### 2.根据类型查找提交记录

> 请求URL：https://csxy-yiban.cn/api/app215/admin_215/type_select/
>
> 请求方法：'POST'

参数：

| 参数名       | 类型             | 必须 | 描述     |
| ------------ | ---------------- | ---- | -------- |
| access_token | string           | 是   | 用户密钥 |
| select_type  | Array (二维数组) | 是   | 主题类型 |

请求示例：

```JSON
{
    "access_token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "select_type": [
        ["doc", 1], 
        ["doc", 2], 
        ["doc", 3]
    ]
}
```

返回示例：

```JSON
{
    "message": "success",
    "recodes": [
        {
            "stuid": "202035020128",
            "recode_id": 1,
            "upload_name": "xxxxx.docx",
            "upload_type": "中国故事,诗歌作品",
            "upload_state": "待审核",
            "create_time": "2021-11-23T14:49:23"
        },
        {
            "stuid": "202035020128",
            "recode_id": 2,
            "upload_name": "xxxxx.docx",
            "upload_type": "中国故事,诗歌作品",
            "upload_state": "待审核",
            "create_time": "2021-11-23T16:08:33"
        },      
        {
            "stuid": "202035020128",
            "recode_id": 3,
            "upload_name": "xxxxx.docx",
            "upload_type": "中国故事,诗歌作品",
            "upload_state": "待审核",
            "create_time": "2021-11-23T20:43:21"
        }
     ]
}
```

##### 3.设置选中作品的状态

> 请求URL：https://csxy-yiban.cn/api/app215/admin_215/set_state/
>
> 请求方法：'POST'

参数：

| 参数名       | 类型   | 必须 | 描述                   |
| ------------ | ------ | ---- | ---------------------- |
| access_token | string | 是   | 用户密钥               |
| set_recode   | Array  | 是   | 改变的作品ID和审核状态 |

返回示例：

```JSON
{
    "message": "success"
}
```

##### 4.下载结果表格

> 请求URL：https://csxy-yiban.cn/api/app215/admin_215/downloads/
>
> 请求方法：'POST'

参数：

| 参数名       | 类型   | 必须 | 描述     |
| ------------ | ------ | ---- | -------- |
| access_token | string | 是   | 用户密钥 |

返回示例：

```JSON
{
    "message": "success"
}
```

