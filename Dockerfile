# 使用官方的 Miniconda 镜像作为基础镜像
FROM continuumio/miniconda3

# 设置工作目录
WORKDIR /app

# 将当前目录下的所有文件复制到容器的 /app 目录下
COPY . /app

# 设置环境变量，确保 Python 输出直接打印到控制台，不会被缓存
ENV PYTHONUNBUFFERED 1


# 创建一个新的 Conda 环境，并安装依赖
RUN conda create -n myenv python=3.8
ENV CONDA_DEFAULT_ENV=myenv
ENV CONDA_PREFIX=/opt/conda/envs/myenv
ENV PATH /opt/conda/envs/myenv/bin:$PATH

# 安装 Conda 依赖
COPY environment.yml /app/environment.yml
RUN conda env update -f environment.yml

# 如果你的项目依赖于特定的 Python 包，确保在 environment.yml 文件中列出它们
# RUN conda install -n myenv opencv

# 声明运行时监听的端口
EXPOSE 8000

# 设置环境变量，以便 Django 知道不要在生产环境中运行数据库迁移
ENV DJANGO_SECRET_KEY=your_secret_key_here

# 设置默认命令，当容器启动时运行
CMD ["python", "manage.py", "runserver", "0.0.0.0.0:8000"]