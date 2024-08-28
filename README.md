
# polyfit 一次/二次拟合工具


## 说明

本程序主要功能为读取待拟合的数据文件，文件格式可以为.txt 或者.csv格式，以空格分隔，无头部。
通过命令行 `polyfit` [filename] 执行,如果未指定文件名，则默认寻找当前目录下的 `data.txt`

数据样本为N行两列的数据，第一列为x, 第二列为Y,
实例数据如下：

```text

   0.134	2.79
   0.160	3.39
   0.195	4.09
   0.244	5.19
   0.313	6.59
```

## 命令行执行
调用 `polyfit [data.txt]`

执行结果如下：

![拟合图形](https://github.com/archeno/polyfit/blob/main/images/fitting.png?raw=true)
