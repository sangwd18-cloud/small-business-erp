# 小型企业 ERP 系统

一个为小型企业设计的轻量级企业资源规划系统，包含财务、库存、销售、采购等核心功能。

## 🎯 功能模块

- **财务管理** - 发票、收付款、财务报表
- **库存管理** - 进出库、库存查询、库存预警
- **销售管理** - 订单管理、客户管理、销售统计
- **采购管理** - 采购单、供应商管理、采购统计
- **用户管理** - 用户认证、权限控制
- **数据分析** - 业务仪表板、报表生成

## 🛠️ 技术栈

- **后端**: Python 3.9+ + Django 4.0+
- **前端**: Vue.js 3 + Element Plus
- **数据库**: SQLite（开发）/ PostgreSQL（生产）
- **API**: Django REST Framework

## 📂 项目结构

```
small-business-erp/
├── backend/                 # 后端代码
│   ├── erp/                # 主项目配置
│   ├── apps/               # 各功能模块
│   │   ├── users/          # 用户管理
│   │   ├── finance/        # 财务管理
│   │   ├── inventory/      # 库存管理
│   │   ├── sales/          # 销售管理
│   │   └── purchasing/     # 采购管理
│   ├── manage.py
│   └── requirements.txt
├── frontend/               # 前端代码
│   ├── src/
│   │   ├── components/    # 组件
│   │   ├── views/         # 页面
│   │   ├── api/           # API 调用
│   │   └── main.js
│   └── package.json
├── docs/                   # 文档
├── .gitignore
└── README.md
```

## 🚀 快速开始

### 后端安装

```bash
# 进入后端目录
cd backend

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 数据库迁移
python manage.py makemigrations
python manage.py migrate

# 创建超级用户
python manage.py createsuperuser

# 运行服务器
python manage.py runserver
```

后端地址: http://localhost:8000
管理后台: http://localhost:8000/admin

### 前端安装

```bash
# 进入前端目录
cd frontend

# 安装依赖
npm install

# 开发服务器
npm run dev
```

前端地址: http://localhost:5173

## 📖 API 文档

启动后端后访问: http://localhost:8000/api/

## 🔐 默认登录信息

- 用户名: admin
- 密码: 创建超级用户时设置

## 📝 开发指南

详见 [开发文档](./docs/DEVELOPMENT.md)

## 📄 许可证

MIT License

## 👥 贡献

欢迎提交 Issue 和 Pull Request！

---

**需要帮助？** 查看 [常见问题](./docs/FAQ.md)
