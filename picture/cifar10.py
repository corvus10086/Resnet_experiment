import matplotlib.pyplot as plt
import numpy as np

plain18 = [0.294, 0.3369, 0.3589, 0.3918, 0.3563, 0.4605, 0.4768, 0.4732, 0.5188, 0.4424, 0.4879, 0.4935, 0.5156,
           0.5196, 0.5117, 0.5037, 0.5209, 0.5489, 0.5497, 0.566, 0.5275, 0.5882, 0.551, 0.4986, 0.4398, 0.5848, 0.5759,
           0.612, 0.5952, 0.5987, 0.5429, 0.5631, 0.6471, 0.672, 0.7036, 0.6525, 0.6313, 0.6446, 0.6756, 0.6287, 0.6694,
           0.6825, 0.6821, 0.6709, 0.6466, 0.7236, 0.7326, 0.7351, 0.749, 0.73, 0.7093, 0.7291, 0.701, 0.7369, 0.6993,
           0.6764, 0.6961, 0.6874, 0.687, 0.774, 0.7612, 0.779, 0.7676, 0.7686, 0.7573, 0.7679, 0.7414, 0.693, 0.7487,
           0.7529, 0.775, 0.7634, 0.7783, 0.7953, 0.8011, 0.7927, 0.8045, 0.7925, 0.7736, 0.7881, 0.8048, 0.7939,
           0.7791, 0.79, 0.8011, 0.8027, 0.7817, 0.7874, 0.7858, 0.7748, 0.7612, 0.7935, 0.7817, 0.7463, 0.7846, 0.7844,
           0.8205, 0.8094, 0.8035, 0.8073, 0.8005, 0.8176, 0.7862, 0.8071, 0.8096, 0.8135, 0.8104, 0.8185, 0.8256,
           0.8049, 0.8226, 0.8279, 0.8151, 0.8178, 0.8267, 0.8283, 0.8242, 0.8265, 0.8149, 0.8243]
plain34 = [0.1444, 0.2141, 0.1944, 0.177, 0.2364, 0.2094, 0.2097, 0.1952, 0.154, 0.1671, 0.1987, 0.2497, 0.2195, 0.2423,
           0.1885, 0.2197, 0.2523, 0.2242, 0.186, 0.1706, 0.1704, 0.1722, 0.2298, 0.1714, 0.2723, 0.103, 0.0991, 0.103,
           0.1859, 0.1457, 0.1434, 0.1576, 0.149, 0.1094, 0.0518, 0.1265, 0.1302, 0.1654, 0.1731, 0.19, 0.2191, 0.2675,
           0.2058, 0.1565, 0.2153, 0.3072, 0.2646, 0.1549, 0.1485, 0.1927, 0.18, 0.1003, 0.1877, 0.164, 0.2075, 0.2084,
           0.2422, 0.2513, 0.2342, 0.26, 0.3341, 0.2584, 0.2358, 0.1623, 0.2544, 0.2318, 0.2499, 0.166, 0.2625, 0.1944,
           0.274, 0.2599, 0.2481, 0.3099, 0.3676, 0.3132, 0.2927, 0.3162, 0.2472, 0.2879, 0.2307, 0.1769, 0.3282, 0.316,
           0.2611, 0.249, 0.2707, 0.3172, 0.2506, 0.2704, 0.2546, 0.2718, 0.3428, 0.357, 0.2921, 0.2595, 0.2716, 0.2723,
           0.3223, 0.1635, 0.256, 0.2793, 0.2684, 0.1918, 0.2095, 0.2034, 0.2589, 0.2867, 0.1899, 0.3091, 0.1985,
           0.2559, 0.3829, 0.2544, 0.2268, 0.198, 0.2588, 0.3869, 0.3607, 0.275]

resnet18 = [0.3805, 0.4437, 0.4718, 0.5412, 0.5613, 0.5813, 0.6023, 0.6138, 0.6341, 0.6348, 0.6893, 0.646, 0.6543,
            0.7004, 0.7019, 0.7119, 0.6744, 0.6572, 0.6755, 0.6658, 0.6781, 0.6201, 0.7295, 0.7125, 0.7238, 0.7075,
            0.6973, 0.6525, 0.6963, 0.7054, 0.713, 0.74, 0.6964, 0.717, 0.7299, 0.7246, 0.7211, 0.7402, 0.7275, 0.6861,
            0.713, 0.7205, 0.707, 0.7251, 0.7129, 0.7351, 0.7176, 0.7497, 0.7228, 0.7293, 0.7212, 0.7193, 0.7129,
            0.7142, 0.6632, 0.714, 0.6846, 0.689, 0.7635, 0.7844, 0.7543, 0.7763, 0.7708, 0.7393, 0.7568, 0.769, 0.7651,
            0.7508, 0.7903, 0.7441, 0.762, 0.7656, 0.774, 0.7729, 0.7812, 0.7883, 0.7586, 0.7565, 0.7906, 0.824, 0.8271,
            0.8165, 0.8187, 0.8166, 0.8189, 0.8095, 0.8004, 0.8165, 0.8141, 0.7962, 0.8202, 0.8455, 0.846, 0.852,
            0.8381, 0.8482, 0.8433, 0.8387, 0.8431, 0.8408, 0.8438, 0.8426, 0.8484, 0.8428, 0.8619, 0.8627, 0.8623,
            0.8648, 0.865, 0.8539, 0.8663, 0.8563, 0.8536, 0.8613, 0.8607, 0.8614, 0.8638, 0.8592, 0.8552, 0.8707]
resnet34 = [0.1948, 0.2892, 0.3743, 0.4517, 0.476, 0.4686, 0.5647, 0.5667, 0.5942, 0.625, 0.636, 0.6357, 0.6588, 0.6682,
            0.6495, 0.668, 0.6775, 0.6381, 0.6667, 0.7096, 0.7052, 0.6959, 0.6722, 0.695, 0.6683, 0.6835, 0.6791,
            0.6992, 0.698, 0.7129, 0.6909, 0.7242, 0.6642, 0.7344, 0.6937, 0.724, 0.7166, 0.7123, 0.7114, 0.7414,
            0.7134, 0.709, 0.6988, 0.7289, 0.733, 0.7336, 0.7123, 0.6692, 0.6811, 0.724, 0.7678, 0.7774, 0.7649, 0.7852,
            0.7617, 0.7787, 0.7689, 0.7537, 0.7789, 0.7657, 0.7878, 0.76, 0.7692, 0.7763, 0.7659, 0.7685, 0.77, 0.7661,
            0.7848, 0.7757, 0.7759, 0.8143, 0.8187, 0.8205, 0.8169, 0.8125, 0.817, 0.8164, 0.8259, 0.8132, 0.8257,
            0.8046, 0.8087, 0.8208, 0.8271, 0.8056, 0.8204, 0.8267, 0.8188, 0.8427, 0.8361, 0.8498, 0.8461, 0.853,
            0.8526, 0.8515, 0.8559, 0.8457, 0.843, 0.833, 0.859, 0.8465, 0.8444, 0.8472, 0.8473, 0.8394, 0.8494, 0.8475,
            0.8525, 0.8486, 0.8495, 0.8684, 0.8697, 0.8692, 0.8679, 0.8699, 0.8662, 0.8725, 0.8669, 0.8732]
resnet50 = [0.0971, 0.2073, 0.2974, 0.353, 0.3916, 0.3894, 0.4199, 0.46, 0.419, 0.4449, 0.4687, 0.5234, 0.5092, 0.5216,
            0.5551, 0.5753, 0.5968, 0.6225, 0.6066, 0.6334, 0.6018, 0.5946, 0.6137, 0.642, 0.6481, 0.6235, 0.6639,
            0.6559, 0.646, 0.63, 0.6523, 0.6723, 0.7028, 0.6581, 0.6827, 0.6436, 0.6519, 0.6693, 0.686, 0.687, 0.6957,
            0.6623, 0.675, 0.7548, 0.7485, 0.7476, 0.743, 0.7614, 0.7279, 0.7263, 0.7127, 0.7493, 0.7305, 0.7438,
            0.7491, 0.7291, 0.753, 0.7578, 0.8129, 0.8066, 0.8086, 0.787, 0.7977, 0.808, 0.7944, 0.792, 0.7777, 0.7942,
            0.8105, 0.808, 0.8102, 0.8093, 0.8161, 0.8098, 0.8089, 0.7816, 0.8211, 0.8161, 0.8054, 0.8189, 0.7979,
            0.8018, 0.7942, 0.8218, 0.7958, 0.823, 0.7896, 0.8123, 0.8158, 0.8116, 0.8197, 0.817, 0.8165, 0.807, 0.851,
            0.8515, 0.8506, 0.8426, 0.8496, 0.8517, 0.8465, 0.8457, 0.8404, 0.8465, 0.8515, 0.8443, 0.8582, 0.8521,
            0.8487, 0.8411, 0.8529, 0.8442, 0.8425, 0.8415, 0.8283, 0.8334, 0.8444, 0.8718, 0.875, 0.8712]
resnet101 = [0.1118, 0.1636, 0.1839, 0.2598, 0.302, 0.3255, 0.3713, 0.3863, 0.4279, 0.4186, 0.4449, 0.4494, 0.4701,
             0.4628, 0.5121, 0.4749, 0.5144, 0.5412, 0.5663, 0.5454, 0.5376, 0.5793, 0.5082, 0.5599, 0.5718, 0.5892,
             0.5619, 0.5366, 0.5767, 0.5537, 0.6301, 0.5772, 0.5817, 0.6094, 0.5874, 0.5957, 0.589, 0.5727, 0.6148,
             0.6099, 0.6229, 0.6874, 0.6209, 0.6534, 0.6127, 0.6546, 0.6713, 0.6525, 0.6881, 0.6508, 0.6816, 0.6646,
             0.7224, 0.6989, 0.7397, 0.7353, 0.7275, 0.7201, 0.7183, 0.6902, 0.726, 0.7281, 0.706, 0.745, 0.7548,
             0.7263, 0.7234, 0.7515, 0.7427, 0.7262, 0.7229, 0.7186, 0.7452, 0.7234, 0.7449, 0.7885, 0.7927, 0.7882,
             0.7983, 0.7884, 0.7914, 0.8025, 0.7957, 0.793, 0.7959, 0.8078, 0.8019, 0.7878, 0.7959, 0.7904, 0.7758,
             0.7956, 0.7636, 0.7882, 0.7832, 0.7965, 0.8227, 0.8327, 0.8204, 0.8293, 0.8314, 0.8334, 0.8328, 0.838,
             0.8328, 0.8338, 0.8173, 0.838, 0.8265, 0.8254, 0.8219, 0.8272, 0.8089, 0.8265, 0.8257, 0.8272, 0.8262,
             0.8261, 0.8544, 0.8563]

plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示为方块的问题
plt.rcParams['font.sans-serif'] = ['SimHei']

fontdict = {'weight': 'normal', 'family': 'Times New Roman', 'size': 20}
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
x = np.arange(1, 121)
axes[0].plot(x, plain18, 'g', label="plain18")
axes[0].plot(x, plain34, 'r', label="plain34")
axes[0].legend()
# 开启网格
axes[0].grid(True)
axes[0].set_title('验证集上的正确率')
axes[0].set_xlabel("训练轮数")
axes[0].set_ylabel("正确率")

axes[1].plot(x, resnet18, label="resnet18")
axes[1].plot(x, resnet34, label="resnet34")
axes[1].plot(x, resnet50, label="resnet50")
axes[1].plot(x, resnet101, label="resnet101")
axes[1].legend()
# 开启网格
axes[1].grid(True)
axes[1].set_title('训练集上的正确率')
axes[1].set_xlabel("训练轮数")
axes[1].set_ylabel("正确率")

fig.tight_layout()
plt.show()
