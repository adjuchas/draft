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

| 序号 | 名称 | 数据类型 | 长度 | 允许空值 | 主键 | 说明 |
| ---- | ---- | -------- | ---- | -------- | ---- | ---- |
|      |      |          |      |          |      |      |
|      |      |          |      |          |      |      |
|      |      |          |      |          |      |      |

##### 数据表2：

| 序号 | 名称 | 数据类型 | 长度 | 允许空值 | 主键 | 说明 |
| ---- | ---- | -------- | ---- | -------- | ---- | ---- |
|      |      |          |      |          |      |      |
|      |      |          |      |          |      |      |
|      |      |          |      |          |      |      |

-----

### 测试接口

##### 用户端

##### 1.回调接口

> 请求URL:'https://csxy-yiban.cn/api/app215/oauth/app215/'
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
    "all_recode": []
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
            "stuid": "201935030150",
            "recode_id": 110,
            "upload_name": "诗歌献给党.docx",
            "upload_type": "时代印记,诗歌作品",
            "upload_state": "待审核",
            "create_time": "2021-11-23 14:25:04"
        },
        {
            "stuid": "201935120133",
            "recode_id": 111,
            "upload_name": "我的大学.docx",
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
    "access_token": "c10d92d219747cf44912fc6bd6362a6894bd198e",
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
            "stuid": "201930010129",
            "recode_id": 113,
            "upload_name": "生在党旗下.docx",
            "upload_type": "中国故事,诗歌作品",
            "upload_state": "待审核",
            "create_time": "2021-11-23T14:49:23"
        },
        {
            "stuid": "202140070103",
            "recode_id": 115,
            "upload_name": "传承红色基因，担当复兴使命.docx",
            "upload_type": "中国故事,诗歌作品",
            "upload_state": "待审核",
            "create_time": "2021-11-23T16:08:33"
        },      
        {
            "stuid": "202140070110",
            "recode_id": 128,
            "upload_name": "百年风华正茂.docx",
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

