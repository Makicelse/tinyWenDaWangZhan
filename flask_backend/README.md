# Backend Deployment Notes

（依赖包管理 requirements.txt 暂时通过手动添加来进行管理。）
- Root Directory: backend
- Python Version: 3.12.2 (see runtime.txt)
- Entry File: app.py
- Required Files:
  - requirements.txt
  - Procfile（暂时先在 Railway 中的 Settings 设置）
  - runtime.txt（指定 Python 版本）
- Secret Keys managed via Railway Environment Variables
