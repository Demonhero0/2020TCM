# TCM
采用DRF框架的中医食疗推荐系统后台
## 使用
### 准备
需要安装[python3.7](https://www.python.org/), [pip3](https://pypi.org/project/pip/), [virtualenv](https://virtualenv.pypa.io/en/latest/)
### 克隆仓库
```bash
$ git clone https://github.com/SYSU-MATHZH/drf-starter.git
$ cd drf-starter
```
### 安装
```bash
$ virtualenv venv -p python3.7
$ source venv/bin/activate
(venv) $ pip install -Ur requirements/local.txt
(venv) $ python manage.py makemigrations
(venv) $ python manage.py migrate
(venv) $ deactivate
```
### 启动 && 开发
```bash
$ source venb/bin/activate
(venv) $ python manage.py runserver 0.0.0.0:8000
```
启动后访问 http://localhost:8000/api/docs

`CTRL+C`停止服务器
### (可选)通过docker-compose
需要安装[docker](https://www.docker.com/)及[docker-compose](https://docs.docker.com/compose/)（或直接安装docker-desktop 包含了docker及docker-compose）
```bash
$ cd docker
$ docker-compose up
```
启动后访问 http://localhost:8000/api/docs

`CTRL+C`停止服务器

#### 停止并卸载container
```bash
$ docker-compose down
```

## API
| url | 参数 | 返回值 |
| ---- | ---- | ---- |
| /api/check | centent | |
