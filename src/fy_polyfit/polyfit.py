"""
本文件通过简单的例子展示了numpy的多项式曲线拟合功能
和matplotlib的绘图功能，主要内容如下：
1. 通过 numpy.loadtxt() 读取data.txt 文件（包含待拟合数据）
    0.134	2.79
    0.160	3.39
    0.195	4.09
    0.244	5.19
    0.313	6.59
2. 通过 numpy.polyfit() 分别进行一次/二次曲线拟合

3. 分别计算均方根值误差

4. 分别绘制 两个图，并显示公式和均方根误差

"""
import os
import argparse
import numpy as np
import matplotlib.pyplot as plt

__version__ = '1.0.2'

# 计算均方根误差函数
def  cal_rmse(y_true, y_pred):
    return np.sqrt(np.mean((y_pred - y_true) **2))


def PolyfitLinear(x, y):
     return np.polyfit(x, y, 1)

def PolyfitQuadratic(x, y):
     return np.polyfit(x, y, 2)

def main():
    parser = argparse.ArgumentParser(description='从指定文件中读取数据,默认为data.txt, 无头部,空格分隔,两列')
    parser.add_argument('filename', nargs='?', default='data.txt', 
                        help='数据文件名')
    args = parser.parse_args()
    filename = args.filename
    # 读取 数据
    try:
        # 检查文件是否存在
        if not os.path.isfile(filename):
            raise FileNotFoundError(f"文件'{filename}'不存在!")
        
        # 尝试读取数据
        df = np.loadtxt(filename)
        print(f"数据文件'{filename}'读取成功：")
        print(df)
        x = df[: , 0]
        y = df[:, 1]

        # 二次曲线拟合
        coefficients2 = np.polyfit(x, y, 2)

        #一次曲线拟合
        coefficients1 = np.polyfit(x, y, 1)

        #打印参数
        print(f"linear coefficients: {coefficients1}")
        print(f"Quadratic coefficients: {coefficients2}")
        # 获取拟合的多项式系数
        a1, b1 = coefficients1
        a2, b2, c2 = coefficients2

        polynomial1 = np.poly1d(coefficients1)
        polynomial2 = np.poly1d(coefficients2)



        x_fit = np.linspace(min(x), max(x), 100)
        y_fit1 = polynomial1(x_fit)
        y_fit2 = polynomial2(x_fit)

        rmse1 = cal_rmse(y, polynomial1(x))
        rmse2 = cal_rmse(y, polynomial2(x))



        formula1 = f'y = {"-" if a1 < 0 else ""} {abs(a1):.2f}x'\
                f' {"+" if b1>=0 else "-"} {abs(b1):.2f}'
        formula2 = f'y = {a2:.2f}x^2 {"+" if b2>=0 else "-"} {abs(b2):.2f}x'\
                f' {"+" if c2>=0 else "-"} {abs(c2):.2f}'


        # 创建2个子图
        """
        创建1行2列的子图，figsize 控制整个图的大小
        """
        fig, ax = plt.subplots(1,2, figsize=(10,5))



        #绘制原始数据点和一次拟合曲线
        ax[0].scatter(x, y, label='source points')
        ax[0].plot(x_fit, y_fit1, color='red',label=f" Linear Fitted Curve, rmse = {(rmse1 *100)/np.mean(y):.2f}%")
        ax[0].set_title('Linear Curve Fitting')
        ax[0].set_xlabel('x')
        ax[0].set_ylabel('y')
        ax[0].legend()
        ax[0].grid(True)
        ax[0].text(0.5, 0.8, formula1,color='red',fontsize=16, transform=ax[0].transAxes, verticalalignment='top', horizontalalignment='center')

        #绘制原始数据点和二次拟和曲线
        ax[1].scatter(x, y, label='source points')
        ax[1].plot(x_fit, y_fit2, color='blue',label=f" Quadratic Fitted Curve, rmse = {(rmse2 * 100)/np.mean(y):.2f}%")
        ax[1].set_title('Quadratic Curve Fitting')
        ax[1].set_xlabel('x')
        ax[1].set_ylabel('y')
        ax[1].legend()
        ax[1].grid(True)
        # transform 变换到[0,1] 的坐标系下，方便定位，左下角0,0, 右上角1，1
        ax[1].text(0.5, 0.8, formula2,color='blue',fontsize=16, transform=ax[1].transAxes, verticalalignment='top', horizontalalignment='center')

        plt.tight_layout()
 
        # plt.draw()
        # 保存图片到images文件夹下
        plt.savefig('../../images/fitting.png')
        plt.show()
    
    except FileNotFoundError as e:
        print(e)
    
    except ValueError as e:
        print(f"发生了意外错误：{e}")

    

if __name__ == '__main__':
    main()