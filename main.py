import sys
from PySide6  import QtCore,QtGui,QtWidgets
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *#导入库
import webbrowser
import segyio
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from modern_1_ui import *#导入ui

from ui_functions import *#导入自定义函数

class MainWindow(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)#隐藏原始系统边框
        
        UIFunctions.uiDefinitions(self)
        #Page1链接
        self.ui.Page1_button.clicked.connect(self.displaystack0)#链接不同页面
        self.ui.Page1_button.setToolTip('This is page1')#设置提示
        #用stylesheet设置具体的色彩
        self.ui.Page1_button.setStyleSheet('color: rgb(153, 113, 113);background-color: rgb(237, 236, 208)')
        
        self.ui.Page2_button.clicked.connect(self.displaystack1)
        self.ui.Page2_button.setToolTip('Skip to Page2')#设置提示
        #用stylesheet设置具体的色彩
        self.ui.Page2_button.setStyleSheet('color: rgb(153, 113, 113);background-color: rgb(237, 236, 208)')
        
        self.ui.Page3_button.clicked.connect(self.displaystack2)
        self.ui.Page3_button.setToolTip('Skip to Page3')#设置提示
        self.ui.Page3_button.setStyleSheet('color: rgb(153, 113, 113);background-color: rgb(237, 236, 208)')
        
        self.ui.Search_but.clicked.connect(self.search)
        
        self.ui.Page1_but2.clicked.connect(self.logging)
        
        self.timer = QTimer(self)#获取QT时间显示
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        
        #self.ui设置提示窗口
        self.ui.btn_minimize.setToolTip('Mininize')
        self.ui.btn_close.setToolTip('Close')
        #链接功能函数区
        self.ui.Page1_openfile.clicked.connect(self.openfile)
        self.ui.Page1_openfile.clicked.connect(self.data)
        self.ui.Page1_savefile.clicked.connect(self.savefile)
        
        self.ui.Page1_but1.clicked.connect(self.show_data)
        
        #page3
        self.ui.page3_but1.clicked.connect(self.show_range)
        #点击设置最大值
        self.ui.Rows_max.clicked.connect(self.Row_max)
        self.ui.Clumns_max.clicked.connect(self.Clumns_max)

        self.show()
        
    def displaystack0(self):#链接不同页面
            self.ui.stackedWidget.setCurrentIndex(0)
    def displaystack1(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def displaystack2(self):
        self.ui.stackedWidget.setCurrentIndex(2)   
    #search
    def search(self):
        query=self.ui.Search_con.text()
        webbrowser.open(f"https://www.baidu.com/s?wd={query}")
        
    
    #鼠标拖动
    def mousePressEvent(self,event):
        if event.button()==Qt.LeftButton and self.isMaximized() ==False:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos()#获取鼠标相对窗口位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))#更改鼠标图标
    def mouseMoveEvent(self,mouse_event):
        
        if UIFunctions.returnStatus()==1:
            UIFunctions.maximize_restore(self)#return窗口状态
    
        if Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos()-self.m_Position)#更改窗口位置
            mouse_event.accept()

    def mouseReleaseEvent(self,mouse_event):
        self.m_flag=False
        self.setCursor(QCursor(Qt.ArrowCursor))
        
    
    def openfile(self):#打开文件
        # filePath = QFileDialog.getExistingDirectory(
        #     # self.centralWidget,  # 父窗口对象
        #     # "选择存储路径",  # 标题
        #     # r'C:/Users/user/Desktop'  # 起始目录
        # )
        # self.ui.line_path.setText(filePath)
        filePath1,_ = QFileDialog.getOpenFileName(
            # self.centralWidget,  # 父窗口对象
            # "选择你要上传的图片",  # 标题
            # r"d:\\testsdk",  # 起始目录
            # "图片类型 (*.png *.jpg *.bmp)"  # 选择类型过滤项，过滤内容在括号中
        )
        self.ui.line_path.setText(filePath1)
        print(filePath1)
        with segyio.open(filePath1,'r',ignore_geometry=True) as f:
            f.mmap()# mmap方法可以加速数据读取
            h1 = f.text[0]  # f.text[0]文件头第一部分
            h2 = f.bin  #需要转换为ASCII码后才能显示
            h3 = f.header
            nTrace=f.tracecount
            nSample=f.bin[segyio.BinField.Samples]
            startT=0
            nInterval=f.bin[segyio.BinField.Interval]#  微秒（us）形式的采样间隔
            nSortingCode = f.bin[segyio.BinField.SortingCode] # 道分选码（即集合类型）
            nFormat = f.bin[segyio.BinField.Format]  # 数据采样格式编码
            print(f'number of trace ={nTrace}')
            print(f'number of samples ={nSample}')
            print(f'start samples ={startT}')
            print(f'sampling rate ={nInterval}')
            print("///reading segy-formatted seismis data:")
            print(f'data file-->[{filePath1}]')
            self.ui.plainTextEdit.setPlainText("///reading segy-formatted seismis data:\n"
                                                f'data file-->[{filePath1}]\n'
                                                f'number of trace ={nTrace}\n'
                                                f'number of samples ={nSample}\n'
                                                f'start samples ={startT}\n'
                                                f'sampling rate ={nInterval}(微秒)us\n'
                                                f'sampling length={nInterval*0.001*nSample}ms')
            
            data2D=np.asarray([np.copy(x) for x in f.trace[:]]).T
        my_data=[data2D,nTrace,nSample,startT,nInterval]
        data2D=my_data[0]
        
        df=pd.DataFrame(data2D[:,:])#转换为dataframe数据
        
        model = PandasModel(df)#
        # Load data into the model
        
        self.ui.tableView.setModel(model)#设置模型        
        # Set table properties
        self.ui.tableView.setSortingEnabled(True)
        self.ui.tableView.horizontalHeader().setStretchLastSection(True)
        # self.ui.tableView.
        f.close()
        
    def savefile(self):#保存文件
        filePath2, _ = QFileDialog.getSaveFileName(
            # self.centralWidget,  # 父窗口对象
            # "保存文件",  # 标题
            # r"d:\\testsdk",  # 起始目录
            # "json类型 (*.json)"  # 选择类型过滤项，过滤内容在括号中
        )
        with open(filePath2, 'w', encoding='utf8') as f:
            f.write('aaa')#write后面是文件内容
        self.ui.line_path2.setText(filePath2)
        print(filePath2)
    def show_data(self):
        import matplotlib.pyplot as plt
        path=self.ui.line_path.text()
        with segyio.open(path,'r',ignore_geometry=True) as f:#segyio提取数据体
            f.mmap()
            nTrace=f.tracecount
            nSample=f.bin[segyio.BinField.Samples]
            data2D=np.asarray([np.copy(x) for x in f.trace[:]]).T
            
        fig,axes=plt.subplots(1,2)
        # plt.style.use('Solarize_Light2')
        # axes.plot(data2D[0:200,1])
        clip=1e+2
        vmin,vmax=-clip,clip
        # from wiggle.wiggle import wiggle 
        # wiggle(data2D)
        axes[0].imshow(data2D,cmap=plt.cm.seismic,extent=[0,1,0,1],interpolation='nearest',vmin=vmin,vmax=vmax)
        axes[0].set_xlabel(f'trace.range:{nTrace}')
        axes[0].set_ylabel(f'data.nSample:{nSample}')
        axes[0].set_xticks([])
        axes[0].set_yticks([])
        
        axes[1].imshow(data2D,cmap=plt.cm.bone,extent=[0,1,0,1],vmin=vmin,vmax=vmax)
        axes[1].set_xlabel(f'trace.range:{nTrace}')
        axes[1].set_ylabel(f'data.nSample:{nSample}')
        axes[1].set_xticks([])
        axes[1].set_yticks([])

        
        plt.show()
    
    def show_range(self):
        path=self.ui.line_path.text()
        with segyio.open(path,'r',ignore_geometry=True) as f:#segyio提取数据体
            f.mmap()
            data2D=np.asarray([np.copy(x) for x in f.trace[:]]).T
        raw_start=self.ui.spinBox_row_start.value();raw_end=self.ui.spinBox_row_end.value()
        colum_start=self.ui.spinBox_columns_start.value();colums_end=self.ui.spinBox_columns_end.value()
        #将ui界面红spinbox数值获取
        plt.figure(1)#显示原始曲线
        plt.plot(data2D[int(colum_start):int(colums_end),int(raw_start):int(raw_end)])
        plt.xlabel('series')
        plt.ylabel('Amplitude')
        plt.figure(2)#wiggle显示图像
        from wiggle.wiggle import wiggle 
        # wiggle(data2D[int(colum_start):int(colums_end),int(raw_start):int(raw_end)],sf=1)
        from scipy.signal import hilbert
        def agc(data, window_size):
                    """实现自动增益控制(Automatic Gain Control)AGC算法"""
                    
                    # 计算每个窗口的均方根值
                    rms = np.sqrt(np.mean(np.square(data), axis=0))
                    
                    # 计算每个样本点的振幅
                    amplitude = np.abs(hilbert(data))
                    
                    # 计算每个样本点的增益因子
                    gain = window_size / (rms + 1e-6)
                    
                    # 对每个样本点进行增益调整
                    for i in range(len(data)):
                        data[i, :] *= gain / amplitude[i, :]
                    
                    return data
        wiggle(agc(data2D[int(colum_start):int(colums_end),int(raw_start):int(raw_end)],100),sf=0.5)        
        plt.xlabel('trace')
        plt.ylabel(' trace sample')
        plt.title('Wiggle Show plot')
        #选择计算频谱的区域
        freq=np.fft.fft2(data2D[int(colum_start):int(colums_end),int(raw_start):int(raw_end)])
        # 将频谱移动到中心
        freq_shifted = np.fft.fftshift(freq)
        plt.figure(3)
        # figure3计算频谱的振幅
        amplitude_spectrum = np.abs(freq_shifted)
        # 绘制频谱图
        plt.imshow(amplitude_spectrum,extent=[0,1,0,1])
        plt.colorbar()
        plt.xlabel('trace')
        plt.ylabel('series')
        plt.xticks([])
        plt.yticks([])
        plt.show()

    def data(self):
        path=self.ui.line_path.text()
        with segyio.open(path,'r',ignore_geometry=True) as f:#segyio提取数据体
                f.mmap()
                data2D=np.asarray([np.copy(x) for x in f.trace[:]]).T
        return data2D
    def Row_max(self):
        path=self.ui.line_path.text()
        with segyio.open(path,'r',ignore_geometry=True) as f:#segyio提取数据体
            f.mmap()
            nTrace=f.tracecount
            nSample=f.bin[segyio.BinField.Samples]
            # data2D=np.asarray([np.copy(x) for x in f.trace[:]]).T
        self.ui.spinBox_row_end.setValue(nTrace)
        # self.ui.spinBox_columns_end.value.set(nSample)
    def Clumns_max(self):
        path=self.ui.line_path.text()
        with segyio.open(path,'r',ignore_geometry=True) as f:#segyio提取数据体
            f.mmap()
            nTrace=f.tracecount
            nSample=f.bin[segyio.BinField.Samples]
            # data2D=np.asarray([np.copy(x) for x in f.trace[:]]).T
        self.ui.spinBox_columns_end.setValue(nSample)   
    
    def logging(self):
        import datetime
        now = datetime.datetime.now()
        
        self.ui.plainTextEdit_2.setPlainText(f'Current date and time is:{now.strftime("%Y-%m-%d %H:%M:%S")}\n'
                                                'This area is empty')
        # 输出一些文本
    def showTime(self):
        current_datetime = QDateTime.currentDateTime()

        # Format the current date and time as a string
        formatted_datetime = current_datetime.toString("yyyy-MM-dd hh:mm:ss")

        # Set the label's text to the formatted date and time
        self.ui.label_6.setText(formatted_datetime) 
class PandasModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, parent=QModelIndex()):
        return self._data.shape[0]

    def columnCount(self, parent=QModelIndex()):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return str(self._data.iloc[index.row(), index.column()])

        return QColor(Qt.white) if role == Qt.BackgroundRole else None

    def headerData(self, section, orientation, role=Qt.DisplayRole):#headerdata它用于返回模型的行或列的标题信息。
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])
            if orientation == Qt.Vertical:
                return str(self._data.index[section])

        return None

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def setData(self, index, value, role=Qt.EditRole):
        if role == Qt.EditRole:
            self._data.iloc[index.row(), index.column()] = value
            self.dataChanged.emit(index, index)
            return True
        return False
if __name__=='__main__':
    app=QApplication(sys.argv)
    windows=MainWindow()
    sys.exit(app.exec())
