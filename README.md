---
documentclass: ctexart
CJKmainfont: WenQuanYi Micro Hei
title: 关于选择 MPEG4 还是 H264 的调研报告
author: wzy
institute: USTC
---

## 条件

为了公平起见，mpeg4 (codec 使用 libxvid) 和 h264 (codec 使用 libx264) 均设置为：

1. 相邻 2 个 P/I 帧间插入 3 个 B 帧
2. 平均比特率为 300k/600k, 误差不超过 2k

## 比较

### 客观结果

从 MSE 和 PSNR 的结果来看，h264 与 mpeg4 差别不大。例如下表是 `crew_cif.yuv` 以
mpeg4 和 h264 编码后的前 5 帧的比较结果。比如前 3 帧 mpeg4 比 h264 好一点，后 2
帧 mpeg4 比 h264 差一点。

```
n:1 mse_avg:9.45 mse_y:11.95 mse_u:3.88 mse_v:5.03 psnr_avg:38.38 psnr_y:37.36 psnr_u:42.25 psnr_v:41.11
n:2 mse_avg:13.19 mse_y:16.05 mse_u:7.08 mse_v:7.89 psnr_avg:36.93 psnr_y:36.08 psnr_u:39.63 psnr_v:39.16
n:3 mse_avg:11.52 mse_y:14.65 mse_u:4.66 mse_v:5.86 psnr_avg:37.52 psnr_y:36.47 psnr_u:41.44 psnr_v:40.45
n:4 mse_avg:37.09 mse_y:51.05 mse_u:6.51 mse_v:11.83 psnr_avg:32.44 psnr_y:31.05 psnr_u:40.00 psnr_v:37.40
n:5 mse_avg:67.65 mse_y:93.97 mse_u:9.07 mse_v:20.94 psnr_avg:29.83 psnr_y:28.40 psnr_u:38.55 psnr_v:34.92
```

```
n:1 mse_avg:12.47 mse_y:16.46 mse_u:3.76 mse_v:5.22 psnr_avg:37.17 psnr_y:35.97 psnr_u:42.38 psnr_v:40.95
n:2 mse_avg:25.15 mse_y:32.76 mse_u:9.99 mse_v:9.88 psnr_avg:34.13 psnr_y:32.98 psnr_u:38.14 psnr_v:38.19
n:3 mse_avg:14.24 mse_y:18.97 mse_u:4.01 mse_v:5.55 psnr_avg:36.60 psnr_y:35.35 psnr_u:42.10 psnr_v:40.69
n:4 mse_avg:14.79 mse_y:19.57 mse_u:4.42 mse_v:6.08 psnr_avg:36.43 psnr_y:35.22 psnr_u:41.68 psnr_v:40.29
n:5 mse_avg:15.12 mse_y:20.19 mse_u:4.22 mse_v:5.72 psnr_avg:36.34 psnr_y:35.08 psnr_u:41.88 psnr_v:40.56
```

### 主观结果

PSNR 只能衡量失真的程度，并不与人眼的观察感受完全一致。例如图 [mpeg4](#mpeg4)
和 [h264](#h264) 是 `crew_cif.yuv` 以 mpeg4 和 h264 编码后的最后一帧的图像。

![mpeg4](images/mpeg4.png "mpeg4"){#mpeg4}

![h264](images/h264.png "h264"){#h264}

### 结论

建议更换。

## 平均比特率

```
mpeg4/300k/crew_cif.mp4           300 kbps
mpeg4/300k/deadline_cif_300.mp4   300 kbps
mpeg4/300k/harbour_cif.mp4        300 kbps
mpeg4/300k/pamphlet_cif_300.mp4   300 kbps
mpeg4/300k/paris_cif_300.mp4      301 kbps
mpeg4/300k/silent_cif_300.mp4     300 kbps
mpeg4/300k/students_cif_300.mp4   300 kbps
mpeg4/600k/crew_cif.mp4           600 kbps
mpeg4/600k/deadline_cif_300.mp4   600 kbps
mpeg4/600k/harbour_cif.mp4        600 kbps
mpeg4/600k/pamphlet_cif_300.mp4   602 kbps
mpeg4/600k/paris_cif_300.mp4      599 kbps
mpeg4/600k/silent_cif_300.mp4     600 kbps
mpeg4/600k/students_cif_300.mp4   600 kbps
h264/300k/crew_cif.mp4            300 kbps
h264/300k/deadline_cif_300.mp4    301 kbps
h264/300k/harbour_cif.mp4         300 kbps
h264/300k/pamphlet_cif_300.mp4    301 kbps
h264/300k/paris_cif_300.mp4       301 kbps
h264/300k/silent_cif_300.mp4      300 kbps
h264/300k/students_cif_300.mp4    301 kbps
h264/600k/crew_cif.mp4            600 kbps
h264/600k/deadline_cif_300.mp4    600 kbps
h264/600k/harbour_cif.mp4         600 kbps
h264/600k/pamphlet_cif_300.mp4    600 kbps
h264/600k/paris_cif_300.mp4       599 kbps
h264/600k/silent_cif_300.mp4      600 kbps
h264/600k/students_cif_300.mp4    600 kbps
```

## 目录结构

```
.
├── docs  // 标准参考文件
│   └── *.pdf
├── get-psnr.sh  // 运行此脚本可重新生成所有视频和日志
├── h264  // 生成的 h264 格式的视频
│   ├── 300k
│   │   └── *.mp4
│   └── 600k
│       └── *.mp4
├── logs  // 记录了所有生成视频的 MSE 和 PSNR 的日志
│   ├── h264
│   │   ├── 300k
│   │   │   └── *.log
│   │   └── 600k
│   │       └── *.log
│   └── mpeg4
│       ├── 300k
│       │   └── *.log
│       └── 600k
│           └── *.log
├── mpeg4  // 生成的 mpeg4 格式的视频
│   ├── 300k
│   │   └── *.mp4
│   └── 600k
│       └── *.mp4
├── README.md  // 本文档
└── yuv  // 原始的 yuv 格式的视频
    └── *.yuv

15 directories, 67 files
```
