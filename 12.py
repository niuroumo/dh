import pandas as pd
from sklearn import metrics
from xgboost.sklearn import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

import pickle

def XgbTrain(X, y):
    train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=0.3, random_state=0)  ##test_size测试集合所占比例
    test_preds = pd.DataFrame({"label": test_y})
    clf = XGBClassifier(
        learning_rate=0.3,  # 默认0.3 学习率
        n_estimators=50,  # 树的个数
        max_depth=10, #树的最大深度
        objective='multi:softmax',
        min_child_weight=3,
        gamma=0.3, #伽玛参数
        eta=0.1,
        subsample=0.7, #训练集占比
        colsample_bytree=0.6,
        nthread=4,  # cpu线程数
        scale_pos_weight=1,
        reg_alpha=1e-05,
        reg_lambda=1,
        num_class=10,
        seed=10
    )
    clf.fit(train_x, train_y)
    test_preds['y_pred'] = clf.predict(test_x)
    test_preds['cha'] = test_preds['y_pred'] - test_preds['label']
    test_preds.to_csv('E:/xinyong/xgbmodelfile/result191-501.csv', index=None)
    stdm = metrics.accuracy_score(test_preds['label'], test_preds['y_pred'])
    import matplotlib.pyplot as plt  # 画出预测结果图
    p = test_preds[['label', 'y_pred']].plot(subplots=True, style=['b-o', 'r-*'])
    plt.show()
    return stdm, clf

train_data = pd.read_csv(r'E:/xinyong/q2.csv', encoding='ANSI')
y = train_data['等级基础']
y = y.as_matrix()
X = train_data.iloc[:, 4:]
X = X.as_matrix()
stdm, clf = XgbTrain(X, y)
path = r'E:/xinyong/xgbmodelfile/xgb1116.pkl'
with open(path, 'wb') as f:
    pickle.dump(clf, f)
print(stdm)