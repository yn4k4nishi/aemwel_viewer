# AEMWEL Viewer
**Description:** 測定結果を表示するためのもの
### プロットのフォーマット
- cartesian2D : 直行座標のXYプロット
- polar : 極座標プロット
- heatmap : 色による3次元プロット

### 対応ファイル
- csv
    - コメントは先頭に`!`
    - ヘッダー部分(1行)に続いてデータ部分が続く
    - heatmapの場合は `x,y,z,f1,f2,f3,...`の形式が必要
- ~~Touch Stone(.sNp)~~
    - 対応予定

## Dependencies
- python3
    - matplotlib
    - numpy
    - cx_freeze

## Install

## Usage
1. 上部のタブから`Form`を選ぶ
2. 上部のタブから`File` > `Open` で表示するファイルを選択する
    - note : heatmap用のデータはファイル 


