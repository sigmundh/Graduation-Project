from flask import Flask
import pandas as pd
from flask import Flask,render_template,redirect,session
import pymysql
import requests
from flask import request
import traceback


app = Flask(__name__)
app.secret_key = 'helloworld'

@app.route('/Forecast')

def Analysis():
    db = pymysql.connect(host="localhost", user="root", password="LQW1107@python", database="modeldata", charset="utf8")
    cursor = db.cursor()
    sql = """
    select * from modelInfo
    """
    cursor.execute(sql)
    results = cursor.fetchall()
    modeinfo = []
    for i in range(len(results)):
        modeinfo.append(list(results[i]))

    return render_template('method.html')

@app.route('/index')

def index():
    i = session.get('user')
    if not i:
        return redirect('/index')


    # data_origin = pd.read_csv('data.csv', header=0, low_memory=False, infer_datetime_format=True, engine='c',
    #                           index_col=['date'])
    #
    # # date = (data_origin.index.map(str) + ' '+data_origin['hour'].map(str)+':00').tolist()
    # # data_origin.index = pd.to_datetime(data_origin.index) + pd.to_timedelta(data_origin['hour'], unit='h')
    # data_col = data_origin.columns.tolist()
    # data = []
    # for i in range(6):
    #     data.append(data_origin[data_col[i]].tolist())
    # data_sum = data_origin.apply(lambda x: sum(x), axis=0).tolist()
    # data_count = len(data[0])

    # date = []
    # date.append(data_origin.index.tolist())
    # if not user_info:
    #     return redirect('/login')

    # dataset = pd.read_csv("LD_MT200_hour.csv", header=0, low_memory=False, infer_datetime_format=True, engine='c',
    #                           index_col=['date'])
    # values = data_origin.values.astype('float32')
    # data_origin['ELE_SUM'] = (values[:, 1] + values[:, 2] + values[:, 3] + values[:, 4] + values[:, 5] + values[:, 6])
    # date_1 = (dataset.index.map(str) + ' ' + data_origin['hour'].map(str) + ':00').tolist()
    # data_col_1 = dataset.columns.tolist()
    # data_1 = []
    # data_1.append(data_origin[data_col[i]].tolist())
    y = request.args.get('week')
    x = 0
    if y != None:
        x = int(y)

    h = x*24
    k = h+24
    data_origin = pd.read_csv('LD_MT200_hour.csv', header=0, low_memory=False, infer_datetime_format=True, engine='c',
                              index_col=['date'])
    data_origin = data_origin.iloc[h:k]
    # date = (data_origin.index.map(str) + ' '+data_origin['hour'].map(str)+':00').tolist()
    # data_origin.index = pd.to_datetime(data_origin.index) + pd.to_timedelta(data_origin['hour'], unit='h')
    data_col = data_origin.columns.tolist()
    data = []
    for i in range(6):
        data.append(data_origin[data_col[i]].tolist())
    data_sum = data_origin.apply(lambda x: sum(x), axis=0).tolist()



    return render_template('index.html',data=data, data_sum=data_sum)





@app.route('/login')

def getLoginRequest():
    if request.method == 'POST':
        return  render_template('login.html')
    db = pymysql.connect(host="localhost", user="root", password="LQW1107@python", database="flaskuser",charset="utf8")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    user = str(request.args.get('user'))
    sql = "select * from userInfo where userID=" + str(request.args.get('user')) + " and userPWD=" + str(request.args.get('pwd'))+" "
    try:
        # 执行sql语句
        cursor.execute(sql)
        results = cursor.fetchall()
        print(len(results))
        if len(results) == 1:
            session['user'] = user
            return redirect('/index')
        # return render_template('/login')
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        traceback.print_exc()
        db.rollback()
    # 关闭数据库连接
    db.close()

    return render_template('login.html')


@app.route('/logout')

def logout():
    del session['user']
    return redirect('/login')




@app.route('/')
def login_default():
    return redirect('/login')



if __name__ == '__main__':
    app.run(debug=True)

