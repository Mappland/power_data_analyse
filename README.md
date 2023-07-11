# 基于NASA POWER能源计划数据综合分析

## [LICENSE](./LICENSE)
 - 本程序所遵循 [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0.html) 开源许可协议
 - 本程序使用的数据集所使用的相关命名规范约定：
   - [CF-1.8](http://cfconventions.org/Data/cf-conventions/cf-conventions-1.8/cf-conventions.html)
   - [ACDD-1.3](https://wiki.esipfed.org/Attribute_Convention_for_Data_Discovery_1-3)
 - 本程序使用的数据集相关协议：
   - The data was obtained from the National Aeronautics and Space Administration (NASA) Langley Research Center (LaRC) Prediction of Worldwide Energy Resource (POWER) Project funded through the NASA Earth Science/Applied Science Program.
   - The data was obtained from the POWER Project's Monthly 9.0.1 version on 2023/07/11.
   - [NASA Open Source Agreement 1.3](https://spdx.org/licenses/NASA-1.3.html)
   - [NASA Prediction Of Worldwide Energy Resources](https://power.larc.nasa.gov/)



## 项目文件结构
```markdown
|-- power_data_analyse
    |-- LICENSE
    |-- main.py
    |-- poetry.lock
    |-- pyproject.toml
    |-- README.md
    |-- .cache
    |   |-- data_com_img.jpg
    |   |-- data_img.jpg
    |   |-- heat_map.jpg
    |-- files
    |   |-- power_901_monthly_2017_ceres_utc.nc
    |   |-- power_901_monthly_2018_ceres_utc.nc
    |   |-- power_901_monthly_2019_ceres_utc.nc
    |   |-- power_901_monthly_2020_ceres_utc.nc
    |   |-- power_901_monthly_2021_ceres_utc.nc
    |   |-- test.jpg
    |-- power_data_analyse
    |   |-- base_map.py
    |   |-- data_analyse.py
    |   |-- data_comprehensive_analysis.py
    |   |-- data_set.py
    |   |-- nc_data.py
    |   |-- __init__.py
    |-- tests
        |-- cache.py
        |-- test.py
        |-- __init__.py
```



## 项目文件说明

- `power_data_analyse`文件夹下文件为每个封装模块
  - `base_map.py`	为热力图绘制文件
  - `data_analyse.py`	为数据基础分析文件
  - `data_comprehensive_analysis.py`	为数据综合分析文件
  - `data_set.py`  与 `nc_data.py`	为 `.nc`文件处理与规范化调用文件
- `files`文件夹下为数据集及开头占位图片
  - `power_901_monthly_2017_ceres_utc.nc`
  - `power_901_monthly_2018_ceres_utc.nc`
  - `power_901_monthly_2019_ceres_utc.nc`
  - `power_901_monthly_2020_ceres_utc.nc`
  - `power_901_monthly_2021_ceres_utc.nc`
  - `test.jpg`
- `test`文件夹下为测试时产生的程序
- `main.py`文件为本程序主文件



## 环境变量

- Python 3.11.1
- Poetry (version 1.5.1)
- 详情见`./pyproject.toml[tool.poetry.dependencies]`



## 使用方法（需切换目录至本项目根目录）

- 本项目使用`python.poetry`包管理器进行包管理及处理，故需先安装``poetry`，并将默认虚拟环境位置设置为本项目文件夹下

  ```shell
  pip install poetry
  poetry config virtualenvs.in-project true
  ```

- 请自行在本项目根目录下创建`.cache`文件夹

- 请自行在本项目根目录下的`files`文件夹内下载相应数据集

  ```shell
  wget https://power-datastore.s3.amazonaws.com/v9/monthly/2017/power_901_monthly_2017_ceres_utc.nc
  wget https://power-datastore.s3.amazonaws.com/v9/monthly/2018/power_901_monthly_2018_ceres_utc.nc
  wget https://power-datastore.s3.amazonaws.com/v9/monthly/2019/power_901_monthly_2019_ceres_utc.nc
  wget https://power-datastore.s3.amazonaws.com/v9/monthly/2020/power_901_monthly_2020_ceres_utc.nc
  wget https://power-datastore.s3.amazonaws.com/v9/monthly/2021/power_901_monthly_2021_ceres_utc.nc
  ```

- 使用`poetry`包管理器进行虚拟环境及依赖项安装

  ```shell
  poetry env use python3.11
  poetry install
  ```

- 运行本程序

  ```shell
  poetry run python main.py
  ```

  
