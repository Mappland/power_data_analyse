# import tkinter
# from tkinter import ttk
#
#
# # 按键处理函数
# def button_process_clean():
#     stringvar_item.set("")
#     stringvar_year.set("")
#     stringvar_func.set("")
#
#
# # 按键处理函数
# def button_process(iiem_val, year_val, func_val):
#     pass
#
#
# if __name__ == "__main__":
#     app = tkinter.Tk()
#     app.geometry("1000x480")
#     app.resizable(True, True)
#     app.title("测试程序")
#
#     # 文本框初始化与放置
#     label_year = tkinter.Label(app, text="所选年份:", font=("微软雅黑", 20))
#     label_name = tkinter.Label(app, text="项目名称:", font=("微软雅黑", 20))
#     label_func = tkinter.Label(app, text="处理方式:", font=("微软雅黑", 20))
#     label_name.place(x=40, y=100)
#     label_year.place(x=40, y=150)
#     label_func.place(x=40, y=200)
#
#     # 选项框初始化与放置
#     stringvar_item = tkinter.StringVar(app, "")
#     content_item = tkinter.Entry(app, textvariable=stringvar_item, font=("微软雅黑", 20), width=11)
#     content_item.place(x=170, y=100)
#
#     # 年份下拉列表初始化与放置
#     stringvar_year = tkinter.StringVar(app, "")
#     combo_year = ttk.Combobox(app, values=["2017", "2018", "2019", "2020", "2021"],
#                               textvariable=stringvar_year, font=("微软雅黑", 20), width=10)
#     combo_year.place(x=170, y=150)
#
#     # 函数下拉列表与初始化放置
#     stringvar_func = tkinter.StringVar(app, "")
#     combo_func = ttk.Combobox(app, values=["热力图", "5年平均值折线图", "12个月综合数据概览"],
#                               textvariable=stringvar_func, font=("微软雅黑", 20), width=10)
#     combo_func.place(x=170, y=200)
#
#     # 按键放置
#     button_clear = tkinter.Button(app, text="清除", font=("微软雅黑", 20), width=7,
#                                   command=lambda: button_process_clean())
#     button_clear.place(x=40, y=280)
#     button_generate = tkinter.Button(app, text="生成", font=("微软雅黑", 20), width=7,
#                                      command=lambda: button_process(stringvar_item, stringvar_year, stringvar_func))
#     button_generate.place(x=40, y=280)
#
#     app.mainloop()
