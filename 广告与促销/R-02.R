library(car)  # 线性回归函数包
library(lattice)  # 做图包

# 读入数据并创建数据框
dodgers <- read.csv("dodgers.csv")
print(str(dodgers))

# 定义一个ordered day-of-week变量，为了画图和数据描述性统计
dodgers$ordered_day_of_week<-with(dodgers,
    ifelse(dodgers$day_of_week=='Monday',1,
    ifelse(dodgers$day_of_week=='Tuesday',2,
    ifelse(dodgers$day_of_week=='Wednesday',3,
    ifelse(dodgers$day_of_week=='Thursday',4,
    ifelse(dodgers$day_of_week=='Friday',5,
    ifelse(dodgers$day_of_week=='Saturday',6,7
           )))))))
#将日期转化为因子变量
dodgers$ordered_day_of_week <- factor(dodgers$ordered_day_of_week, levels=1:7,
                  labels=c("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"))
