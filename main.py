import os
import tkinter
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import power_data_analyse as pa

# 全局变量声明
label_image = None
image = None
photo = None
stringvar_img = None


# 图片显示函数 打死不要动！！！！！
def image_show(in_app, in_image_path):
    global label_image
    global image
    global photo
    # image_path = r"D:\Project\Pycharm_project\power_data_analyse\files\test.jpg"
    image_path = in_image_path
    try:
        image = Image.open(image_path)
        # 将jpg图片转换为tkinter可用的格式
        photo = ImageTk.PhotoImage(image)
        label_image = tkinter.Label(in_app, image=photo, height=700)
        label_image.place(x=500, y=-100)
    except:
        image_path = r"D:\Project\Pycharm_project\power_data_analyse\files\test.jpg"
        # 打开jpg图片
        image = Image.open(image_path)
        # 将jpg图片转换为tkinter可用的格式
        photo = ImageTk.PhotoImage(image)
        label_image = tkinter.Label(in_app, image=photo, height=700)
        label_image.place(x=500, y=-100)


# 清除按键处理函数
def button_process_clean():
    stringvar_item.set("")
    stringvar_year.set("")
    stringvar_month.set("")
    stringvar_func.set("")


# 年份处理函数
def year_val_process(in_year_val):
    if in_year_val == "2017":
        return nc_data_17
    if in_year_val == "2018":
        return nc_data_18
    if in_year_val == "2019":
        return nc_data_19
    if in_year_val == "2020":
        return nc_data_20
    if in_year_val == "2021":
        return nc_data_21


# 生成按键处理函数
def button_process(item_val, year_val, month_val, func_val, in_app):
    if func_val == "热力图":
        try:
            name_nc_select = year_val_process(year_val)
            if month_val == "该年该项目平均值":
                month_val = 12
            else:
                month_val = int(month_val) - 1
            pa.map_paint(name_nc_select, item_val, int(month_val), item_val + " Heat Map")
            image_show(in_app, r"D:\Project\Pycharm_project\power_data_analyse\.cache\heat_map.jpg")
            stringvar_img.set(r"D:\Project\Pycharm_project\power_data_analyse\.cache\heat_map.jpg")
        except:
            tkinter.messagebox.showerror("错误", "请检查输入")
    elif func_val == "5年平均值折线图":
        try:
            name_nc_select = pa.nc_data_set(nc_data_17, nc_data_18, nc_data_19, nc_data_20, nc_data_21)
            pa.data_analyse(name_nc_select, item_val, item_val + " Average Data Preview")
            image_show(in_app, r"D:\Project\Pycharm_project\power_data_analyse\.cache\data_img.jpg")
            stringvar_img.set(r"D:\Project\Pycharm_project\power_data_analyse\.cache\data_img.jpg")
        except:
            tkinter.messagebox.showerror("错误", "请检查输入")

    elif func_val == "综合数据概览":
        try:
            name_nc_select = pa.nc_data_set(nc_data_17, nc_data_18, nc_data_19, nc_data_20, nc_data_21)
            pa.data_comprehensive_analysis(name_nc_select, item_val, item_val + " 5-year data processing")
            image_show(in_app, r"D:\Project\Pycharm_project\power_data_analyse\.cache\data_com_img.jpg")
            stringvar_img.set(r"D:\Project\Pycharm_project\power_data_analyse\.cache\data_com_img.jpg")
        except:
            tkinter.messagebox.showerror("错误", "请检查输入")


if __name__ == "__main__":
    # 文件读取与初始化
    os.chdir(r"./files")
    nc_data_17 = pa.nc_data(r"power_901_monthly_2017_ceres_utc.nc")
    nc_data_18 = pa.nc_data(r"power_901_monthly_2018_ceres_utc.nc")
    nc_data_19 = pa.nc_data(r"power_901_monthly_2019_ceres_utc.nc")
    nc_data_20 = pa.nc_data(r"power_901_monthly_2020_ceres_utc.nc")
    nc_data_21 = pa.nc_data(r"power_901_monthly_2021_ceres_utc.nc")

    # 查看其中一个数据集参数
    for item in nc_data_17.info.items():
        print(item)

    app = tkinter.Tk()
    app.geometry("1200x520")
    app.resizable(True, True)
    app.title("测试程序")

    # 文本框初始化与放置
    label_year = tkinter.Label(app, text="所选年份:", font=("微软雅黑", 20))
    label_month = tkinter.Label(app, text="所选月份", font=("微软雅黑", 20))
    label_name = tkinter.Label(app, text="项目名称:", font=("微软雅黑", 20))
    label_func = tkinter.Label(app, text="处理方式:", font=("微软雅黑", 20))
    label_name.place(x=40, y=100)
    label_year.place(x=40, y=150)
    label_month.place(x=40, y=200)
    label_func.place(x=40, y=250)
    # 项目选项框初始化与放置
    stringvar_item = tkinter.StringVar(app, "")
    content_item = tkinter.Entry(app, textvariable=stringvar_item, font=("微软雅黑", 20), width=11)
    content_item.place(x=170, y=100)

    # 年份下拉列表初始化与放置
    stringvar_year = tkinter.StringVar(app, "")
    combo_year = ttk.Combobox(app, values=["2017", "2018", "2019", "2020", "2021"],
                              textvariable=stringvar_year, font=("微软雅黑", 20), width=10)
    combo_year.place(x=170, y=150)

    # 月份下拉列表初始化与放置
    stringvar_month = tkinter.StringVar(app, "")
    combo_month = ttk.Combobox(app, textvariable=stringvar_month, font=("微软雅黑", 20), width=10,
                               values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
                                       "该年该项目平均值"])
    combo_month.place(x=170, y=200)

    # 函数下拉列表与初始化放置
    stringvar_func = tkinter.StringVar(app, "")
    combo_func = ttk.Combobox(app, values=["热力图", "5年平均值折线图", "综合数据概览"],
                              textvariable=stringvar_func, font=("微软雅黑", 20), width=10)
    combo_func.place(x=170, y=250)

    # 按键放置
    button_clear = tkinter.Button(app, text="清除", font=("微软雅黑", 20), width=7,
                                  command=lambda: button_process_clean())
    button_clear.place(x=55, y=320)

    stringvar_img = tkinter.StringVar(app, " ")
    button_generate = tkinter.Button(app, text="生成", font=("微软雅黑", 20), width=7,
                                     command=lambda: button_process(stringvar_item.get(), stringvar_year.get(),
                                                                    stringvar_month.get(),
                                                                    stringvar_func.get(), app))
    button_generate.place(x=235, y=320)
    image_show(app, stringvar_img.get())
    app.mainloop()
