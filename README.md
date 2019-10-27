# 概要
- コサイン類似度使って検索queryにマッチする論文アブストを取得するプログラムです。

## 環境
- python3.6.8

## 必須ライブラリ
- numpy
- scikit-learn

## 使い方
- cloneしたディレクトリで以下を実行
```shell
$ python main.py query --datafile=./data/abstract.txt
```

### 例
```shell
$ python main.py "multi agent"
コサイン類似度: 0.29504274108756745
アブストラクト: 'it is well known that heterogeneity is an important feature of multi agent systems in this paper we consider the second order consensus of hybrid multi agent system which is composed of continuoustime and discrete time dynamic agents by analyzing the interactive mode of different dynamic agents two kinds of effective consensus protocols are proposed for the hybrid multi agent system the analysis tool developed in this paper is based on algebraic graph theory and system transformation method some necessary and sufficient conditions are established for solving the second order consensus of hybrid multi agent system two examples are also provided to demonstrate the effectiveness of the theoretical results'
```
